from django.shortcuts import render, redirect
from .models import UploadedImages, Faces
import face_recognition
import hashlib
from PIL import Image
from .utils import encode_face_link, decode_face_link


def home(request):
    ctx = {}
    return render(request, 'fdx_search/index.html', ctx)


def search_error(request, err):
    ctx = {}
    ctx['err'] = err
    return render(request, 'fdx_search/search_error.html', ctx)


def search(request):
    ctx = {}
    if request.FILES['file'].size == 0:
        return search_error(request, "Плохой файл")
    hasher = hashlib.md5()
    for chunk in request.FILES['file'].chunks():
        hasher.update(chunk)
    file_md5 = hasher.hexdigest()
    try:
        UploadedImages.objects.get(md5=file_md5)
        return redirect('search_1', slug11=file_md5)
    except Exception:
        pass
    try:
        im = Image.open(request.FILES['file'])
        (width, height) = im.size
    except Exception:
        return search_error(request, "Плохая картинка")
    ctx['file_md5'] = file_md5
    ctx['width'] = width
    ctx['height'] = height
    ui = UploadedImages()
    ui.file = request.FILES['file']
    ui.md5 = file_md5
    ui.width = width
    ui.height = height
    ui.state = 0
    ui.save()
    return redirect('search_1', slug11=file_md5)


def search1(request, slug11):
    ctx = {}
    try:
        ui = UploadedImages.objects.get(md5=slug11)
    except Exception:
        return search_error(request, 'Поиск не найден')
    ctx['image'] = ui
    image = face_recognition.load_image_file(ui.file.path)
    ctx['face_locations'] = []
    face_locations = face_recognition.face_locations(image)
    faces = len(face_locations)
    if faces == 0:
        return search_error(request, 'Не удалось найти лица на фото')
    elif faces == 1:
        (top, right, bottom, left) = face_locations[0]
        return redirect('search_2', slug11=ui.md5, slug22=encode_face_link(0, top, right, bottom, left))
    else:
        cnt = 0
        for top, right, bottom, left in face_locations:
            ctx['face_locations'].append({
                'cnt': cnt,
                'top': top,
                'right': right,
                'bottom': bottom,
                'left': left,
                'width': (right - left),
                'height': (bottom - top),
                'link': encode_face_link(cnt, top, right, bottom, left)
            })
            cnt = cnt + 1
        faces = len(ctx['face_locations'])
        ui.face_count = faces
        ui.save()
        return render(request, 'fdx_search/search1.html', ctx)


def search2(request, slug11, slug22):
    ctx = {}
    try:
        ui = UploadedImages.objects.get(md5=slug11)
    except Exception:
        return search_error(request, 'Поиск не найден')
    ctx['image'] = ui
    image = face_recognition.load_image_file(ui.file.path)
    ctx['face_locations'] = []
    face_locations = face_recognition.face_locations(image)
    cnt = 0
    for top, right, bottom, left in face_locations:
        ctx['face_locations'].append({
            'cnt': cnt,
            'top': top,
            'right': right,
            'bottom': bottom,
            'left': left,
            'width': (right - left),
            'height': (bottom - top),
            'link': encode_face_link(cnt, top, right, bottom, left)
        })
        cnt = cnt + 1
    (num, top, right, bottom, left) = decode_face_link(slug22)
    encoding = face_recognition.face_encodings(image, known_face_locations=face_locations)[num]
    ctx['num'] = num
    ctx['top'] = top
    ctx['left'] = left
    ctx['right'] = right
    ctx['bottom'] = bottom
    ctx['width'] = (right - left)
    ctx['height'] = (bottom - top)
    ctx['encoding'] = encoding
    searched_vec_low = ','.join(str(s) for s in encoding[0:64])
    searched_vec_high = ','.join(str(s) for s in encoding[64:128])
    query = """
            SELECT id, sqrt(
                           power(
                             CUBE(array[{}]) <-> vec_low, 2
                           )
                            +
                           power(
                             CUBE(array[{}]) <-> vec_high, 2)
                           ) AS koof
                           FROM fdx_search_faces
                           ORDER BY
                              koof
                           LIMIT 10
            """.format(searched_vec_low, searched_vec_high)
    ctx['query'] = query
    ctx['results'] = Faces.objects.raw(query)
    return render(request, 'fdx_search/search2.html', ctx)
