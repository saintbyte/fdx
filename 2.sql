 SELECT id,
  sqrt(
 power(
 CUBE(array[
 -0.0860380306839943,-0.011017147451639175,-0.033762119710445404,-0.05846516415476799,-0.12961487472057343,-0.07761989533901215,0.005510738119482994,-0.19992893934249878,0.09840171784162521,-0.09519130736589432,0.13988900184631348,0.030407492071390152,-0.21365496516227722,-0.08075614273548126,0.029293321073055267,0.11802244931459427,-0.09639473259449005,-0.1356799602508545,-0.12065495550632477,-0.14167717099189758,0.03047678992152214,0.05370045080780983,0.0296121034771204,0.025779439136385918,-0.08772547543048859,-0.20346009731292725,-0.10015146434307098,-0.09063076972961426,0.11628786474466324,-0.0335317924618721,0.03213558718562126,0.030664881691336632,-0.20425066351890564,-0.043023984879255295,0.00136647280305624,0.04196615517139435,-0.0653727799654007,-0.13582642376422882,0.16786064207553864,0.03245154768228531,-0.17254887521266937,0.03434181213378906,0.05846625566482544,0.2515312433242798,0.2395252287387848,-0.03193454444408417,0.045190006494522095,-0.04945351928472519,0.08146882057189941,-0.18391166627407074,0.11351493000984192,0.04243570566177368,0.12918514013290405,0.06297671794891357,0.017992042005062103,-0.17168226838111877,0.06413912028074265,0.1368228644132614,-0.2356346696615219,0.10398183763027191,
 0.13518349826335907,-0.11178348958492279,-0.07736212760210037,0.014121918939054012
 ])
 <-> vec_low, 2)
 +
 power(CUBE(array[0.2163427174091339,0.11511898040771484,-0.1126578226685524,-0.12856431305408478,0.13882829248905182,-0.21673348546028137,-0.09273379296064377,0.014340642839670181,-0.14692802727222443,-0.09923863410949707,-0.33723190426826477,0.062479715794324875,0.3940790593624115,0.14860284328460693,-0.16118334233760834,0.007323629222810268,-0.04246693104505539,0.07057517766952515,0.1081080436706543,0.0954035297036171,-0.06597112119197845,-0.08874399960041046,-0.10772932320833206,-0.00733158178627491,0.16355840861797333,-0.0006847372278571129,-0.09307745844125748,0.2680320739746094,0.05679842084646225,-0.0784432590007782,0.0325208455324173,0.09020668268203735,-0.08265361934900284,-0.07872077822685242,-0.030687356367707253,-0.07552837580442429,0.07028595358133316,-0.1303596794605255,0.06010040268301964,0.16944748163223267,-0.16391870379447937,0.20467184484004974,-0.027978960424661636,0.052487812936306,0.047815680503845215,-0.007039091549813747,-0.04175994545221329,-0.0632949024438858,0.06973958015441895,-0.18959331512451172,0.1773594319820404,0.18398380279541016,0.06276112049818039,0.12784574925899506,0.03122396394610405,0.11046648025512695,-0.031181924045085907,0.031470246613025665,-0.15265265107154846,-0.06772003322839737,-0.0029883868992328644,0.029177073389291763,0.080860935151577,0.13562068343162537])
 <-> vec_high, 2)
 ) AS koof
 FROM fdx_search_faces
 WHERE
koof  <= 0.5
 ORDER BY
 koof DESC LIMIT 10