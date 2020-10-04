import unittest
import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.substringDiff(2, 'tabriz', 'torino'), 4)
        self.assertEqual(solution.substringDiff(0, 'abacba', 'abcaba'), 3)
        self.assertEqual(solution.substringDiff(3, 'helloworld', 'yellomarin'), 8)

    def test_case_1(self):
        self.assertEqual(
            solution.substringDiff(
                11,
                'gatezejttddpkmndtauvjcffiiafgzhkqgzliirdldbmqkdfpeadgjxcirgkmkcfxorthhpujbnenxansboejjrqfxoohuolsxgohukxmpzfukzvkduurvajrodlpxojzsihiqftrbkixbcxraqpiyadbkzqihmigunrzfzcgzfkeszcpkdotulkktfduekyqzkymqpeidhpyuhotynqaxknnsheiogrhobrajzkrekexvorlvlyhtgstjrtdgjzahvmjnprcumulnvftgoiyctjgtthleeunkgbemapsntmfdnuaydkrbyngbrbpsznfdftonfmbjahqrpgddbkokvdxfflzysneapnqvsqhilxabbjamkdhpktscxsczpoontmliozurkrvagnidnmcayiradtbacltouzacvseayrdzkkkqgbfrrnfydbnnxvctffgtfpbmfzsqjnclcnttztcvvpbmkovahvpdnjqghcafzcxhrxumhxxkdtyjqypljzsbidfpoydlumdrhokvmstydlmymldvimdduvzzcmiyxapbrrrndhjnhncpibdmiryjteyvcydxkthxcbgxshffuzevvfrcrpzaotcpbefqqppehgdlbfstralgzbtdfervuvejyvvocrabkiohjxjnnrshvyijyonzzioeakpbkgxybtlcbybgzvvvvhhkdfvpupxnlecqizvzhgigliotybprnnntqdsiquxvdxojripdlmzsyorhjandaqtjfptgebxbjmnokevncfxkkadrsqjvxuttokcabefxehmnhkcbgrdmnmmycflifrrkriggeplcfafpxsbfchbdzbvdgsbrcebgkgsdbdntfdbaltnsdzraafhobrsygkvetomeqvkrntyzeqimcaktnvfcehaeexqjnjfyvomfqlbdjxhhjojvytaovvprpfrdpgurzfhknsimnmhctbkzxfxjrzfjvjsigivmlxcgiginjitarxettzzcpceonufetlpdxupmpfmhzanufjxrkaapaaalaulebxizfjshbjsagmxmuesvecuoobuctngykkzsztzauquxxdgmjxuybkzvxsftzpqhmarlsbaeriaahlrcdgjadhbrizmnabcfadtnfdzobdhayhrxmdddycenimblnrlicasqhttekqyiafijoiykcmutzbjupsbqxbzeyqxbsshelvzieoiozylenrlaelpykdpvzhvpttmsyxsjbrfqchgrxcuvkgqinluzjrqlnzitvhlofjiznsxvbbhscsuoufodozsrmjecfdrkcslgmmrcletuvxcdfitpmgocjdcurrbfqpefxtndzkuuzxpaxfanxdxnteiapkzouvqiykxntmltdpmyzjveivnfuhzlrkseyhpbgrtcvnqmpqcgubjyourdrizixmoflmyzsskvfagtdopgthcdmmqhkmksxgeckagmjgauvz',
                'gltezejtfdehkmndtauvicffiiafozhkqmzlieedldbmqjdfpeadgjxcirbkmkcfxorthhpujbnekzansboejjrqfxoohuozsxgohukxmpzbukzvkduurvajrodlpxojzsvhiqftrbgixbcxmaqpiyadbkzqnhmigunrzfzugzfkeszcpbdotulketftuekfqzkymqpeidhpyuhotynqqxknnsheitgrhobrajzkrekexvorlvlyhtmstjrldhjzahvmjnprgtgulhvftgoiyctjgtthleeunkgbemapsntmfdnuaydkrbyigbrbpsknfdftonfmbtahqrpgddbkokvdxfflzysneapnqvsqhilnabbjamkdhpktsxxsczpoontmliozurkrvagnidnmcayiradtbacltouzacvseayrdzkkkqgbfrrnfydbnnxuctfegtfpbmfzsqjnclcnttftcvvpbmkovahvpdnjqghcafzcxhrgumhoxkityjqypljzsbidfcoynlumdrhokvmstydlmymldvimrduvzzcmiyxapbrrrndhjnhncpjbdmiryjteyvcydxkthxcbgxshffyzevvfrcrpzaotcpbefqqppehgdlbfstaalgzbtdfervuvehyvvocrabkioojxjnnrshvyijymnnzioeakpbkgxdbtlobybgzvpvvhhkdcvplpvnlecqizvzhgiglsotobprnnntqdsiquxvdxojripdlmzsyorhjandaqtjfptgegxbjmnokevncfxkladrsqjvxugtokcabeqxehmnhkcbgrdmnmmyfsmifrrkriggeplcfbfpxsbfcxbdzbvdgsbrcebmkpsdbdntfdbaltnsdzrfafhobrsygktetomeqvkrztyzeqimcaktnvfcehaeexqjnjfyvomfqsbdjxhhjojvytaovvirpfrdpgurzfhknsimnmhctbkixfcjrzfjvjsigilmoxcuiginjitarxettzzcpcesnufbtlpdxupmpfmhzqnufjxrkaapaaalaulebxizfjshbjsagmxmueshecuoobzctngykkzsftzatquxxdgmjxuybkzvxsftzpqhmarlsbayriaahlrcdgjadhbrizmnaycfaftnfdzobdhhyhrxvddsycenimblnrcicasqhttekqyiafijoiykcmstzbjupsbqxbzeyqxbsshelvzxekiozylenrlaelpykdpvzhvpttmsyxsjbrfqchgrxcubkgqinluzjrqltzitvhlofjizxsxvbbqbcsuoufodozsrmjecfdricsljmmrcletuvxcxfitpmgocjdcurzbfqpefxtndzkuuzxpaxfanxdxntuiapkzoufqiykxntmlyepmyzjneyvnfuqzlrkseyhpbgrtcpnqmpqcgubjuourdriziimoflmyzsskvfagldopgthcdmmqhrmksxgeckarmjgauvj'
            ), 256)
        self.assertEqual(
            solution.substringDiff(
                5,
                'jbzchixyxcxfqjnjmiasntcprcskiivbfzxjaohtaejmusmefigtzettecygkzzlmlbflkiemsovrqkarzsgrgilxteokjemfhpqabufpliyhizsenlynufjsqnosvdkkciijvxykgjevlxcggfsnbipvephmheeqajkrbemzxlfmetnyrsmtdisrccglfvegxvepghmczavkrqxfoijhqnsihckuhvhdyzjiopzcikryykimvfzesgahkxjgxdfcyjpmvmouegrvjgjoxudpntcpyzsabsaetiaeyvdyttnfunkkpkcnxnpmhtxvnozxplhsqixkrgnpaxtvaojuitdiiixtfschpjfrgoaffolkpfbpsbdacufyqloidkgvuntnuiumvcckrvdepcscenvlaffmldeohhxibznfshehgqevbdljvurefbvvlzlpkvusdibytomjrkcitubfetvqcnlkoghxqpzcfizgzccjponmepcvtvjccfzxnxnhipsnqkqgemmqdeacnphoivlbdqzyafjckepdqokrmkhjzzjbijugnqkaaezbguyhjgtqqpgfbizhjaejllodtusjgbolkrmrynmkdvtzkfaovieccrhlzlusyxchyryzirvnrknrzvfmnilvcxzjauyajhaavprjybsgeijspvjaxugeralbjnccyhimafuiexgftzxjzzizprdmopvximdvjmoshirkvcubjyhdvutzzcmardemkzlpfayclmpatmreoycgeccgcdnbvovvvvhiffodetqthtbenpnhimbyevlqjhqtgjsioazjtelvbpyihclhqayxtgrkkbpmdqggepczzryyrmruulsjgzjzacrcdkmxmobhrcdiatullfczxlvavyrqzgndbozblozqoohtbqlqelbaipcqyykgpdpxkgdyqvhyhuogbtjqkilrmdfhljrugvbljdsqufaclhajkmhydykgxvfvayjlcdeqfhohuuqzofvuamxjgkhjupqkyzxnmxzatpumutgrhippzsjlgjbpfyofrjunpxkfvpjxkqgjsdxaotdqqtjhbmmhcqzskahjcxblcyxdhpfqbbmxuxgydnvvvhmytoshbjghpaqmexflmincpnhutgulmbckqzhilydqnietdmketagxygynpbktvetkaqoihhmlqdiytgdligdoycnnpvpiehngoxqdxqzcjobgtzbmlomptsipinsbapeeqipjievsjazayebtnbuvizgxhimngceavogbzmrmqdkqxatxnbnxnciouljshvgdapdmvvvhejvzphafkvospycdqebvrogfsgdczfrhyqvnkdvxxtsejlvcbpeeajvucllhhpfmqfctdfanbayhglfzrdptgxbnvpqoqmqlidifgmdeklvayxitjiyndhmjujsoqzmxvyjgztrfelxjqlchmgkzmkafttvxgnudkkcqnot',
                'dxehkupglkaajohzbekahlbgcoxkopopcdevojqsaabbozmeykpgcqjsfzhxgdlscldvvsxcrgaxhjpidpcngrarjgbcgdipjpvjnhepaifsvboljiprmapgrffuasaanhmqdficmdtollxdtntzkfqetzrnjvdmayellsvaytstgmzbednrfpkbstaudtboxsphxorsfblihdgyejbomsgjuhlsvfafsdcqzyfqfaafiujdgqlpqgojubrqfkyribrvysvxbcnvxfoysrbveeeohsyzluyjumxrmikeezlxchentzkfvqhsytshyqdzczcphohymlyxlphlzrvocrqigexlbnndtshqmnbekorqobuhcgvziolqzqqkkbialvhgsgyiclmjkxunpjnovkvhzembctticfuhuavsjzfnubdyrfvfbzcxedayytivhuyfhvpcrzsxaxsosmqzhuapfgmdtlaigesrbsxicjtdguchdeucnhtuotpazemxszosafsuymxxzlzohrksdzudtjkbmekakygvmeneqfxquiolsocnhgalcexzjelmisniocdxbsbkejmvbbzayxdrszeruyzfsgoagddalceivzuqhiyfqirqtvkjkkhozlpbthvcqkzglqcgkylxsvoigvuocpkzcydirevjmzgrlixbeyqcvkuxovayjzslhxfolykklurmccrcyacxlzplxinbcotfbronigtfjthoqiuasiylpjmrkklmfeoeiqkguhenzcanqdjffztqigzpbhgisunqdsmbokpnzgextfkbtuzpxjdqtvecsglnprmbzhapkixpgkmpcjybucvgvdaxknhkoldrsrmvtxyamarhgurjridzxhkcxskloleikgcvizaavnccxujcbqmivpzypktxtkropbkfbvqnxdeygjoxhvshvgojpfozmfufzbebsfrqpjbcnostyauchzcryqyofiupgesbnnytnfxgodikltnqicxzutkflxrmloqktglsixsyrrduarsaqjmjlvlgskysycdpibmrrdchtuagvpdhqqasslmunyaizszauduvbhhvgqogxfeedfyycjpabgpxxqgplxyatcghpridotcsdfpuvmqbrqxiadusvskmoflmgyzqivkmizsrjtbkbrstcixtrvlzasnzrjvakuugzcanyffrnvbqmijvsrszmeujouvblcikrknpnmooplxmynulrsyfhbeepgjedexkqusafsmnllirimmtyknkdvacnkjgbetvlomykzeatfrmregvfpicskkaxdbcmcjkadkqqshppmtmaujsthiceyyoicbfrhodvlolelgelsrmsykqlglotlyfxbjderyzsibxlsvpbzfhxbugzvhgavbseevohbmracxoaukpjopeqvjmmcjebcmdqsnctcdonoshumbjmbosadtqpxjaedjhkxulzfyzftxu'
            ), 13)
        self.assertEqual(
            solution.substringDiff(
                959,
                'dtmkpbfpnvpdclsksfauvjhhpcjsllnzyrjgtcglsuhoavvmiqbeuihvmqxomcinobzuyhydcusdpeynunlmicfzbmpclssyuuchzjunquhcxqlzojndmyoypkljtjpocdnabgdzdcxpahfkthlovmfguinvugipqypaoqiloiuhgmmzhlsndbdukjzaqpzxcomvxfjekvbvivfhfiisbzlskzsayjselytupymdkmocsoiflxyskitjjevpkvmjamcihruiotsdjihqaxnbcmoguuperpmmkuryegnfpovpyuxxkppbxqejcnfdpirkmouujctsntudgynbdnytuuiletszvkgjdttnscabhtketezfehyihddmccmaamazvelnulvirmnlixykiyukuseelybeqnluuifchllupknmrqzypxzccypnfumldgsrscaguojfvkxmycuzyzbfozfjxupsboshilnlachrgcjeezqkevtobsbvsqjceoitqcieyvkcaxrbdmsbivsyjllyuuikjhpzxvpprtbbdnagjcoqdzvrlmglqmblecoglnrmmrvsehlnjtjhtmcegcigbggirrvgjjoksokdkkjjgfspcbykbfzcivxjmjyzdunstukdzpiouadfleftacoaurjlytckootvhicqmlhyhuymdexygujpzztebclmjxlmzqglnbkzbegoeiyzvpyvenxptdctghsugddspmahegygdbedajjqjbemafumnhempxpzaybxgkdrvgmhflaeeyeplcbhzfarbzgyeqeoijctltnqvgdfnmueefpxknmokxhfojmoitpcldqovhpnkitkyszqftxpxbsqfobotoqvblyvftbykoffumbrxvtaflnsiyuolyycntyuxyupztbplsxninvsvueavbkeubojktucvqodjzdfjrzqysqvhmhvxgeuvfzzymkqvjxiibcjbkfxitzdxiejjvufgfrcqdjuryoptllcbmyukhhaeedomevxtqsoftgcfzbciqcuqsxfnzciriruptcavexfyxvspustzudsgjfmlsndpsptahtyxngocbctnbysyvyjqpigdkooxrofifncousnypnipspcplayxlmdoyjkczduvrbkxtxzmtqieuedxyvrqayvvphtjzokfkvozqpzoklhgvcjzsbtrlmrookpkzzycfyxkbhnxxoxuqqqpnuorejvqaurqfmxalzxkdrvplovduqbmmmpsmvfuccyeiijtlegojbbquvrxijebxzdevilvzdjvtbsevghfjfzydqpeqobhjzzpclpcpmdnjkvnifatnysblacbcnhscdgicjibrljkxkavdsxjkatklrsrooehmtydvbueacoyiatfhsmatlpzkzqyhqqmotbivgnfugxofrabcmdjeyrcyvllvhxunnzziabdihjdctkdkcvbtplaiofalsqbbhn',
                'dtmcpbfpnvpdclxksfzuvjhhpcjsllnzyrhgtcglsuhoavvmiqbeuihvmqxoecinobzuyhydjusdpeynunlmicfzbmpclssyuuchzjunquhcxqlzojndmyoypkljtjtocdnabgdzdcxpahfkthlovmfgpinvugipqyraoqiloiuhgmmzhrsndbdukjzaqpzxcomvxfjekvyvivfhfiisbzlskzsayjselytupymdkmocsxiflxyskitjjevpkvmjamcihruiotsdjihqaonbcmoguuperpmmkuryegnfpovpyuxxkppbxqejcnglpirkmouujctsntudgynbdnytuuiletszvkgjdttnscabhtketezfehyihddmccmaamadvelnulvirmnlixykiyukuseelybeqnluuifchlluoknmaqzypxzccypnfumldgsrncaguojfvkxmycuzmzbfozfjxupsbosvilnlachrgrjeezqkevtobsbvsqjceoitqcreyvkcatrbdmsbivsyjllyuuikjhpzxvpprtbbdnagjcoqdzvrlmglqmblecoglnrmmrvsehlngtjhtmcegcilbggirrvgjjoksokdkkjjgfspcbykbfzcivxjmjyzdunstuodzpibuadfleftacoaurelytckootvhicqmlhyhuymdexygujpzztebclmrxlmzqglnbkzbegoeiyzvpyvenxptdctghsugydspmahggygdbedajjqjbemafumnhefpxpzaybxgkdrvgmhflaeeyeplcbhzfarbzgyeqeoijctltnqvgdfnmueefpsknmokxhfojmoitpcldqovhpnkitkyszqftxpxbsqfobotoqvblyvftbykoffumbravtaflnsiyuolyycntyuxyupztbplsxninvsvpeavbkeubojktucvqodjzdfjrzqysqvhmhvxgeuvfzzymkqvjxiibcbbkfxntzdklejjvufgcrcqdjurgoptllcbmyukhhajedomevxtqsoftgcfzbciqcuqsxfnzciriruptcavexfyxvspustzudsgjfmnsndpsptahtyysgocbctkbysyvyxqpirdkooxrofifncousnyznipspcplayxlmdoyjkczduvrbkxtxzmtqieuedxyvrqayvvphtqzojfkvozqpzoklhgvcjzsbtrlmvoorpkzzkcfyxkbhnxxoxuqqqpnuorejvqaurqfmxalzxkdrvplozduqbmmmpsmvxuccyeiijjlegojbbluvrxijebxzdeviivzdjvtbsevghfjfzydqpeqobhjzzpclpcpmdnjkvnifatnysblacbcnhscdgicjibrljkxyavdsxjkatklrsrooehmtydvbueacoyiatihsmatlppkzqyhqqmotbivgnfugxofrabcmdjeyrcyvllvhxunnzziaydihjdctkdkcvbtplaiofalsqbbhn'
            ), 1500)
        self.assertEqual(
            solution.substringDiff(
                19,
                'uqtkddfckfgrmiqjqjmiehgtqijpmgczqqaijezenljdcrdzqjpgiagoahmtqrxzkdrytiszecpudicjaekikjrltojeuxsxntbuumlruplujnqmsinpceczzylggztumggjhtekdebuixvdnrldyczloqmyznzkoirhxyigcbjfcjixaqjmjdkzjjhlapzuxumuxarhvycbxxdqhyvmkhcuaeunimekrghfsrsfjqnbtoiupumxlzmjdxpumaycoipuofbqpfsmlzujlemlxvehlrbqcajxrjtdhlhingadbhxraccigxezucgyiocbojbpbbkguudxmpsrbbaykxktaetpegqllgjgcbsshhcvycagilkjoyqkfqxvkugjxtacqmjpmjlyztuiufqzvesaommrjzfjgidlymdfekbtfrmmdhyidtvraxjtkpetzedckufqbuddqrxjhvptkxuqsouuyqjzonqaebiveltlmjbemikynydapcpibygbsarpesjoofzpqmekegkqxftmkoqevqruhyiazfiyzkjejpqhrdfxyequrkitngcuobsnintzqztglpjvnbphefudsemsqrbjzrzcqevbdsttvghpcmjayzbkxfygqmeclosdqcviqyuhlpysfjzelvxbsbcvjnmvhuznpbzeeouzzaarfpikysfdjvlmutmnjuoxushqxpyvvdtisdsfxipgoypcvemevofaytbssyrnaqdzciyloxmfcnpjkojrjsydqvgdborxmbsttcggvhoszyrevojigfjkyboayghpjiobfgtkxlafxhtjaqmfdppbhecmkfvcydylxgqxnvvnrmvjutlbfdhnggygranlushushcmybymspgjhldzecxgxhyiuflvfrpebfsueecnfrggkjdouclrantfdfgqlejprodtqagnxluotcuhzgeryakboocsppgehjirroxqbmmgvocnimojhxapvbojvohrsjzunaivbblkrqlfcqgdmsskuxyvabskudnbrfsyqrtzjphidfofunmkcqkirklnskayxezbadkliraurcifvbrzovbiugzgrmtjoqyodgsjedghvgiizkvrbffqodxiyjogoezbioofyyqoezfirrrkpvmfglqvdkuytyqcsfixfasbmuveelhnnxnlnjgrzihgnjvydsnytxjyqlmqunvgoyrlktukbdayjivxrfiateazyzazpuhkmztmkagellqlozadxfyfgrzecrrkijoplzxbablrgofbqmtpthzextrhbxeuvossikqagrpgfoenobqcbcjvvvrgddbyefrhhqfizqdegakukjbjnvtexudrcvlsisorqmjdsbtspauqvfqlyhfxcponefhehdmjvuyidstrlieujkpljrpvuxpdopkfmaoxyivqmcdberovfkrecnmygtzdjzburoulsdmootcynotqgbjlxkvc',
                'uqfkddfckfgrmvqjqjmiehgkqijpmgczqqaijezenljdcrdzqjpgfagoahetqrxzkdrytibzecpudicjaekikjrltojeuxsxntbuumlrupuujnqmyanpceczzylgyzmumggjhtikdvbuixvdnrgdyczloqmyznzkoirhxyigcbjfvjixaqjmjdkzjjhlapzuxumuxarhhycrxxdqhyvmdhcuaeunigekrghfsrsfjqnbtoiupumxlzmjdxpumaycoipuoobqpfsmlzujbemaxvehlrbqcajxrjhdhlhingadbhxraaxigxezucgxoscbojbpbxkguudxmpsrbbaykxktaetpegqilgjgcbsshhcvycagilkjoyqkfqxvkigjxtacqmjpjjlyztmiufqzvesaommrjzfcgidlymdfekbtcrmmdhyidtvraxjtxpetzedrkufqbuddqrxjhvptkxuqsouuyqjzonqaebiveltlmjbemikynydapcpibygbsfrpesjoofzpqmukegkqxftmkoqevqruhyiazfiyzkmejpqhrdfxyequrkitngcuobsrintzqztglpjvntphefudsemsqrbjzrzcqevbdsttvghpcmjaizbkxfygqmeclosdqcvibyuhlpysfjzelvxbsbcvjnmvhuznpbzeeouzzaarfpilyifdjvlmutmnjuoxushqxhyvvdtisdsfxipgoypcvemevofaytbssyvnaqdzciyxoxmfccpjzojrjsydqvgdborxmbrttcggvhoszyrevojigfjkybogyjhpjiobfgtkxlsfxhtjaqmfdppbhecmkfvnydklngqxnvvxrmvputlbffhnggykraplushushdmybymspgjhldzecxvhhyirflvfrpebfsueecnfrggkjdouclrabtfdfgqlejprodtqagnxluotcuhzgeryakboocqppgehjirroxqcmmgvocnimojpxapvbojvohrsjounaivbblkrqlfcqgdmsskjxyvzbskudnbrfsyqrtajphidfofunmkcqkirklnskayxezbadklkbaurcifvbpzovbiugzzrmlrjqykdgsjedgnvgiizklrbffqqyxiyjogoezbuoofpyxoehfirrrepvmfglqvdkuytyqcsfixfasbmuveelknnxnlnjgbzihgnjvymsnytxkyqlmqunvgoyrlktukbhpyjiexrfiateazyzazpuhkmzimkagellqlozadxfyfguzecrrkijoplzubablrhrfbqmtpghzextrhbxeuvosoikqagrpgfoedobqcbcjvvbrgddbyetrhhqfizqderakukjbjnvtexudrcvlsisorqmjdsbtspauqvfqlyhyxcponefhehdmjvuridstrliepjkpjjbpvuxpdopkfraoxyivqmcdberovfkrecnmygtzdjzbukoulsdmootcynrtqgbjlxkvc'
            ), 429)
        self.assertEqual(
            solution.substringDiff(
                10,
                'kniohjpxezspcoykzurdvfjvmvhkveilxuyxgultaxujcrfktxhvnczhcaduqeiidqagfzxxydsyldupplrdznjqgmcrusdpzhddgoyxeiqzlcclsymoranfbzbarmfryuuiiaxivauoargbyuzfmhzlgojnvdikprzriquohmirvqetjvhmgiqqmepmcpvicjyaqueygfxghvbmsysfrfnmurroehtxlkxhlchiqgfxvzdjeiqfdxbyzntfqudbebmtqzkrunbcozcsfplimsfcuvnnpabtiviyejjvfvlztjutsdzbkelidsccivrrrkdvhfslamchgxakqzehnrrmtdzjyyfzfeofupctagaqdrkiepxjytquxfrftlxxgnsfcoctjjkhycolxsxrrlmoercstpgqeeagegscojgsgkavvfqopgpcbpgehzpcnhkdpatufylcdajkqybdfenbnpksctlsqdhnrinvhxyensmqbyxypqpogzflnjeinadmieheqtizdapaaypbezkxgxepcquyptyvczybqscijluzaxbrsirphssoqbaxsqruuvqkpzdggeoeanzykryodmulxceyfdsouqgpaahgvxmmzooxxipclctfexlgqqtfmkghfompflmpegfbnvvzxismbsvymkcsriqjfdkkemlpaidoitxufxvolyhjelxcrosirkiptopbvqgjcvsihuqqihnmyivgcgcetsqcelitepseejvjrumtmrceupseuisbklikrynnfjubtfmpcyutdgpfkohrdyvxehhrjogtmeqsmilmpmndpbiehciltulstinnkrkuqemjepsbkasiduozeaigxerigjcllnhzztvsyznebaznrgtesxchxobptmpqzpvyqujsamhnxgqxysrynyscnktlmemhlgxoyyfivojudlmmzrcukiyoayuhnrrknilvugovpnvbhpgbzzhhbvjygkrstjsukyyjogtqqcijkqotaxskiujlxitrpaholrefgeaacgsqothofdumfyzlmqikyzydanpsbrlnenbctaxlrdatafseagrsgroxnfrudyzcyxukitsajgdjngtfernpxocyqkleofgozjifxyoqxttglupcdexlbaknuuliqmdslgenllbsbcmjthdmblcrjnfcpckgrmujazxtahqtyihggekysqzhdrdanzhhlxmjsymthaqtzbdzicshhmconryfiitgyzpyudfdscmdfjcusualaahgjvilxiejsdlmurvaliorpdhagqtbtcgeiflttzfnabunytkgqlsavukctesduscaclxocondzadoeshcmnsvgbozfggoytdxhcfuvboqskngxqtkzygnvezomzxdaocxmlqzbvkkxmldcfbxsigduymprnodvehpjerhpogifamsjbdbrbrgqkxlnzzebxtzirsbroxupcajhiqikmlg',
                'kniohjpxezspcoykzurdvfjvmvhkveilxuyxgultaxujcrfktxhvnczhcaduqeiidqagfzxxydsyldupplrdznjqgmcrusdpzhddgoyxeiqzlcclsymoranfbzbarmfryuuiiaxivauoargbyuzfmhzlrojnvdikprzriquohmirvqetjvhmgnqqmepmcpvicjyaqueygfxghvbmsysfrfnmurroehtxlkxhlchiqgfxvzdjeiqfdnbyzntfqudbebutqzkrunbcozcsfplimsfcuvnnpabtiviyegjvfvlztjutsdzbkelidsccivrrrkdvhfslamchgxakqzehnrrmtdhjyyfzfeofupctagaqdrkiepxjytquxfrftlxxgnsfcoctjjkhycolxsxrrlmoercstpgqeeagegscojgsgkavvfqopgpcbpgehzpcnhkdpatufylcdajkqybdfenbnpksctlsqdhnrinvhxyensmqbyxypqpogzflnjeixadmieheqtizdapaaypbezkxgxepcquyptyvczybqscijluzaxbrsirphssoqbaxsqruuvqkpzdggeoeanzykryodmulxceyfdsouqgpaahgvxmmzooxxipclctfexlgqqtfmkghfompflmpegfynvvzxismbsvymkzsriqjfdkkemlpaidoitxufxsolyhjelxcrosirkiptopbvqgjcvsihuqqihnmyivgcgcetsqcelitrpseejvjoumtfrceupaeuisbklikrynnfjubtfmpcyutdgpfkohrdyvxehhrjogtmeqsmilcpmndpbiehciltulstinnkrkuqemjepsbkasiduozeaigxerigjcllnhzztvsyznevaznrgtesxchxobptmpqzpvyqujsamhnxgqxysrynyscnktlmemhlgxoyyfivojudlmmzrcukiyoaauhnrrknilvugovpnvbhpgbzzhhbvjygkrstjsukyyjogtqqcijkqotaxskiujlxitrphholrefgeaacgsqothofdutfyzlmqikyzydanpserlnennctaxtbdatafseagrsghoxnfrudyzcyxukitsajgdjngtfernpxocyqkleofgozjifxyoqxttglupcdexlbaknuuliqmdslgenblbsbcmjthdmblcrjnfcpdkgrmujazxtahqtyihggekysyzhdrdanzhhlxijsymthaqtzxdzicshhmconryfiitgyzpyudfdscmdfjcuaualaahgjvilxiejsderurvaliorpdhagitbucgeiflttzfnabunytkgqlsavukctesduscaclxocondzadoeshcmnsvgbozfggoytdxhcfevboqskngqqtkzygnvezomzxdaocxmlqzbvkkxmddcfbxsigduymprnodvehpjerhpogifamsjbdbrbzgqkxlnzzebxtzirsbroxupcajhiqikmlg'
            ), 752)
        self.assertEqual(
            solution.substringDiff(
                1117,
                'jvuqduqtmazuqasplrupxibmxrvzhchetlqoanoemoyzoitxnyzyazedydhpzyfomqlyqxvykechioojiyenvvxtasxvrqienpgfeudksyuqniddrxtvvfspnrfkirhclujkodazbycufhcgdlttkjbzrpcgosxyhhbuhclvsluiiumfstpqlsgvagqabuurluvfaizcfkvtisopyurnhhnsxiikylkkxmkbuzrpvltedyjomrbldibodcrqgqcinolhohmqsyyxlrldjxxlzcztoekujoyhuhganltursuomgovcjkdxaeekelyjvchgvhkedsbytaphdzrukskddpjlbhvbdgvtajbnohtzocxuezjhupatedpaarexugobjonuffujdcfdcbcsulxsatfzopadhfchsyptvrisdqmsrxmisbtqdssuztjtjzybockeqgihdimkbnuhprcenqsegytjdzpdovckmkdztsazryqcxidkpaxjcjcvsovhrgmechrdnmrgctyxfoflxrgeqqpeezlmcvufhbgjfaeqtqcbqfsalsoqkocutyyjqamgszhphsxosyflaphdngilfamtocrrckpvgrkfajsiotejskmryenkgmmnralfhlcmmevvdkaitrmcqrsdgiotdgzqlekgmbovfjvjpzxzysadacmjeoruccvnprgcngpubnolplnvmjmecxannymgjtahzdtjknltbexrjcirczojlixopzffypunocqhhxtzdvbsvbcjjyaixgoasqqihqfjfdvcxnkpblrrnrsxxzvgppvzpcrjhqzzptdaqchitffectpivxyqqidiqahdxvodifrcbbpkruovfjkvnfjinrhnebiccyuqzsnvmmnlfuvlgmblsjmmyerrmvfbyoxfzljsdxorhbkaycuvmoxvbxhzvficcpkmsxkkvivvzbnktdxiooskkyhupnkjhkbynopaficexqasbolmdyjsmzrobievfpbbtyzkbqriuptnjsavopesbxnqmdpngajdzsyhxcjnkeiltixjhlmzcrcdpghosvsscqdexfbosensnxbiieznhyhxdposxgvbhrssudepkqqxyiqdpgoyidrxbsfulysqrcujuhztcldsxmpfmkfmmjnaotyxxkgnecoqpqbukqegtsmbvraorjhlcxgtkteqxnlzmmshgqoahqcjjhimoivrfnxjvbbxkleylvbhsgmtqlqlmsqhiznlqvxjlubzsjfjlqdxpemiveatjqhsuerimnpjdjfyzjptnrxpolectzcculoqjleixsmuxfvfupuzustixtssaigfgtubbiipzafkepsodmryuiugjesbijehgkbqadtyfasyjgiuppyndlqctytenqftuydfxvdampathlqmfxldsfrsgyfzzonbfnhmakzzpuhnlcbfjuritqkoerbxzkgbflvzfpgeveajzrc',
                'tvgpkxepilojfmuombrpgfvdntqzddtierdxuquufrisdesiyimffjkxpsibxyntxqlpnqppshooheaejhapdsreqrzavfmciisrjsurjokaaejxcuicjukymrxrqdhhzlyrvivljscclksottcirhikekfigrgxbrkhuuzhivbucxnhhzpzaxdyaecjbeulrgmosyumlogidlfcsqxafmfqmrccjkcvarsybiboaenjzcsiylhvprcmsyxnixgncrcfssyfphhskzimutdgtbgfxfqjlnqorqtgvnofmerdadyhofobedzhnjysctrdszfbglmxjtucaxvcxavpnzdvizhrbzpfyhhgbshmprazspvdpsjizumriqxumtryvfivjngthxvcfscjzcypikxouxveyiigichdamlnhbirbnrllassxroisyihpgsafdsrrpjchhoeknnpgudgxddlftvoqgcjlohozpclghejrxosrzuoboygoquqbrjmkjzyofprzasforiadfmcxzffrrfquperyxkoszbayfymjrrdtnrniqrxcixmqxsndjtjvmgqfdoeumotrlomcishfmeuabteprakbhvvhlvmfzobjaaapplsiugymrzdsoeyyifbcjruqcdcqyzcchnrqsbsfzxbevakffikkonpmbhnstbdkeeltqgzcymajdkfrsfettvtkbdzadqtcgktlsdrygqdzdbalmcoohglpaeffaqhnklepuslafojggqbspaybkhfstetscszefuejotvzudynkknbndfvhvasqcugxbqdtfekincxsquyzshuxjjnknnzxjbsogsogflshjyezgypfolgsuaifrvmltjdaxcgqsetzrjmxcnxdxnlnjjkjlqqnxlppzievcbcoanyyvgxeedaxpuzppcmvmrluxocjkxjdmzkhlpgqmhzvhrphyvyeguimnkspnvhgglhoarhtrlzdcbinhmihgqfquzcsotrjmsydytafkaqxtydkqauhbfmadbomjhbffjnhramjkrjrpqnybjztbaimprthdjftipnnkgsigkomuhtfiploikssdebbrluucgoorlavottkiqylfyxslxoafypompicsadmrealbvfmxpiiqdyqvksntnilymlipmkaneteytyfqrqrgtfbqpndbsorvfcyxmovsrrkzudiqjmogaisjnidxsktejtzcjvsmlzbazztyhmvdbbuukqoyyikxtteopezrsfsknxqskfjylyvqflaryhmsrmvtklyfpgapooryjupchsaxxndvzhfeilfxmindbzpjoptyznhnzhhnzssoqucjasyzhisbkfioqnclaaygaqjhejdzhcmvlvhpgsqumlgridvtksilsnpurdevtilmzdkasqkktxsazcsziydrzrnsjhkqhqilynttggmspnrrusxtovnkdqrsobdiaukyzzzgv'
            ), 1191)
        self.assertEqual(
            solution.substringDiff(
                31,
                'uvtedmbqjjazboxbephroffzguecvykbhyafuhsohmetnmdgqpihumsmoxirjrupgnocppctglnmbvolxuubohegeofgshufltgguaymvyoxpmdklbgkdkkzscsxcxcslistafhkzoisxkkqdqavjnuommxxteuxzgfvmusxlsqdueejicvbkizfbvodusbvruqxbcodzybsxazdglvxzzgnsudxfrbtqrfooprbdoxnodpblnlrypdobzgqnsigezdpkhkphonxgabnkgjsvypcrcgehiehljruykpduxoesekjfpbfpxqmyknvrjncmcretfcolzuabqzlezdyopnrsqpuhzzkmgchbsiohnydxydeytxntrpnxhatiqukhsflcifiehccbhjfgnrettuyxktgauboqulrhymjnxzqhcqsfdmmhgiepbbrmhznkfnadvlfplhcszuyzotbxkuysbqleqnypigncvicnjirkvdtdikzdyfmzeccuxmtorcaapjrsahkylcmsejsaumgmlhrofrlvkqglxcnrqmebuuuvaxmatkdnqzoxdkoxuqkrhcoqjbvbmgjrzohthnhqaanngsxqephzmqesecfccsakgznnjmhoucjtebvzigoryroprrmiidxyrtpocniqoalxqhloxcdplhuvthqsyjznbqmantrbxgoqgdnzyhvpovndgkxmsszfbaqkoimnyxsbvavxmkxhkzoedijyspvzsjknrcvradybzeanesxxuzvxmqtjabnmlcnayysgjxrfsjrcjaoyuliehuqyyoxpezfgxxhgsihqomhppjyitiyiyikomklvuoxbkemkervhucidnoynxcyflyqleagpqkgmnquueexspnoxqpapdatsfzzihiusagklunvcvaavslybundctzqdzfercjpjieobdemnnxbivroxkfhdvhqztcrlsvakyhchaluknxkpknoyrbyyrbuidvjlknssyurtvelfxfletkssjgnlveiysfkajkedvmxarptqrxpnitltailrgbcjjhoyyefdgrbbxzijryihyucszdlijikkivckzkipzclefeeypbstotofgnrovyczkeucfmlcxqyjumlavxutlqaxvtyixeshykftrmjxrzmihffngmdtssnkmvkrhveqocynehdysdevpqfpkkequfavldkibfokesqcpjhmuvamkxebfodaczprkhbblnrliullczyeotqmuyzvsibslxnatqtfarkltzjbfsyaysitcsfohbnpjzopnxeknrecknphcoerfgpzxroyvmunryapmjglacplehabtlgfczttgyvilikbinxskheksgfmaxvlgayfjfebtgsmoprknxvhzzmyaotblsdallzpdzkscgteuhfiygojbdotdorfalsxjjnnjvtdacharuhxrthmkpbobvrjcooonqqzpuvmjcsffzx',
                'vlceyrlgrugkjoblzfxneijkrhrfgvytmmesgbcfphagtdezgjazvytozaplhfpeqxbzxefoiknedxvongyslxzlkaeisjbvgsnnauhkiivbfqkpkjiyjsyftrjtkykixfdiojerqebljlqqmttlfzdutumbsgvlohimtajbpppqznxyejzutljuuylastgbykmnyzthyqzvrtjceuhcmnzfzxseaxxzuynzxynipeidmzsroyuahxtkubeecikuayybyxrnzyafxgkazrovhgsypljpclpzqnlfojosubpfhgstvpxylxbjoqlhthiljdcsqugbgxyltydujmqcbpuytzqrbjptomiromzybicefazzmmredurkvgdrqzvdtrrsimpdzxsogsvreflykbrmleebvdxmurmpnxypetrviatqddkbdmggarlndiovgqpkutyjhkagmpcyirkrffyyvxagvpeyhhefsgcfiupmaydlcmegrhejkgmqtldhgudrltepagpgpfxoqplooskudszfvqobcckexqserdduxfmgkypgcsohcmfyrxrbvgggnfhehhkeckttxrpgrlxsrxetcdnsqesvifajnjlhtceiickvneiamkxonftamyuollbfzvjpecaquzimjpjckajvfjzcfgbhzqaougndjbjrgbvyhetpaxfjdlnrlmlstdplpyxggbokhsretpbzrddmgbuksexevratqkagtmacfcfelbpprbvtgipntbgtluuccoxpxexnyellnjcshsprjdliepcdsjjqsemkujlnzeiburrzubtfbdkuolqnoejjfkzmgxgebyygajffjttyeqojsyeeadbbyayrskmgajvexyyyxvxtcqlqsrqlelrdeuxidrpiyfjczjlauseyuqzkcyzoytubljggpbstgvcgqehpciurrjjrpxxhvsmdnrezijvqcvyzsubfidltxhijmtaprjsoieoabzxsqzvtexsxgdxbiztnqlrjocrclecpbsaeszgqzooliazpebzelvdmvxvormexinetkbtcxaxokulrboqlmmcrsrviclyxtgaymxhharimlaanfqpshuadxghtevlcajmtmqtyvokjxccieuaxpsmegmhjuaxlclmblbpkabtqrmrspsippxtydrodctnbignjoyacldgtsotovqqeejbqiaskghqfegdijlrvkdecgxzdfjlolbimzialprvsdnjljqltyczvhbtdoeechkosiydsceenaafvdgkgdlidzzoiogvjnafcsymrrkylnqjkpzvnbzgsarorudfryeitybpaqziltyplfepguixbblvzzqrcmyvfjggpsvtdgccqyfyukyxxycnetjnaavehnuehlvtaifykkazkcklfqllxreltmzmxhcqhizjymdezzjlgussulurgykaeevmpmabjjprnpxvnztfgnbqmbhue'
            ), 40)
        self.assertEqual(
            solution.substringDiff(
                7,
                'sgrycabxpgxocgrecrrcrzvazcrizkcvemqfzuajamvdyuyaokeqtxzmpajartyskeaahtbmnuyypbzhfokdxkdepzjnxzthhajsugjzpgoccgfqeyodajayesypegfhfboplefttahfunxltcqoekvdzrfeeiamkpqgqkpzcglaaxjkelmfeqczysbetkbqegpdxcqsprbfzhkxgkplajqycngiyatssaxambljvakotxbkbhgijuqsdsxtbnltrdnjgltydoxnrpkcnhafpbhzjdttjtfujddxrmbcfhryxbglfyrpvsxocbozzlcjsrkdipkdusztlficensocmbcmtpmkxdixzojspkrinraaeodofyihlvnnyvoknbhnorgckzlqzirgqezshcbkjmibbkocjlrmulykqceyvbvqyfoeitvutqmdpydltjgqzmmbkhzkhgmezdahbfvbmmvvaybqpiooonvrpescrakbjcksbjmvcpeznumdyzrsukptfiylsxfymexspjsglqhdeogvxhyvnarzvbajmszcnpyfnrjrcpndojupclztgcaakfrbfitfvdqnkkeuxvpyyphupfhhiczdceiyacdohauhdgaalzzltuvatcjbrkpnhoqyadulgoqvkpxpqyuxvitedbeongcizzpsvhjesrvcohjrkxutyneeuhocibkzrgkfibmvdfksibjmxsfuvnmcycfddmebafjvgxtvjakbfamqlmqtzvxguktfkqhaugqjaryumqejzkvrucikdgzoshdyquaipzcluartflyfzykkdvinukejnabpnnlgunztdlkirljhuxvxdebjdyjpsfgypzjfuvrtuhgzxaxzlfpxnvvaobbdmszethiozqslkuljebvzyrjvomomhxuitrnjlqmyrfyfsslqymdexhcgtudbadkqximdzfvodtumkdpqgscazausscckqrotrrmzaqrvfzvnsrnfdgsmjufbxgkhyfzbinltupxxdpitfxzdnaqeryeedrssbzsucfsxtckqexhqndkurmukmpsyrhivptfnrxsqjfcllutuzmiiouuksxteskbgupeizgaqxfcipkibiimhbhngxuuvelqkvazfcboliomyobqgxnllknysvugqaxhtstbsjarbpofblxpbnvrdadnfkphukdqpkoqufpueemnhuhgurfhjkullgnqofpshtgodzjoqtjmblqqerhitkccpzfadopjflezipouehvylxrxourrjcpqbxrnnyzkxmhvpccsinqtoygoxqbaqsydrsusxxobgoknsjogkrpskxrfszmnecngtmtbqxptdlkoblhcdkuuhdpiyfzqelmmdkyxvptbbyfdxspunjkxishlmccafshfkjmkdyspjlzikttqpolvtyatlueouejymscvnhqyipmzalahogbvolbqgenjhnoabacoivfirocq',
                'gctqlymshvrzuefrzgoynqytssamjlakhgpvieqteptcpqjlxoqlgzntbhixthtrpvjibqrafoltfmjliyrupduvrqgdngxbxgpqcjthuzxfjbmxjcottxqkhlmsrcmedgxvvdfptuixyxgetvsgtyepcdovepxnorlotfzkflfjurpsrconvfogkeezzmybtgisayldasdrqkrbmimvxxjysvblyihgddsdnvqmerzxcqznnfdcqyiayhsdcsivxdehjnyyrazfrksncuvanbexjkovsyvdvicgumisfgnfmbomgpjixbfijoxhyxoeqvkzehstdhubuhtsstifpipssnkquasbulkdcscxnbyjvsexcdrltflgxzuppvkqmtxbvvsvgrpnalgifulccycoqoptruqtlcdvypvboitbonrirjafnjnovsrfaicdndfcdnzyioodrrxbsqnfgedgzflvjkddhoipmrnlnpevbalyptsjuqbpesnusephmttppzvioxlqrgcfogrfjlccxyyccfzbhgvhcqlqnpizfjxphezfsmvtymbizkqcvmlvkujhlatcnzqzouqfgqlxrkjbgfgihhcpsanzbvosrfzefqfxypjnrfpbutdlqocnvenpteuxhudqvezgvshemlsbihtaopqhrlzphlfcbfcmefahoanmduhqgqhgfavoczobvmkumbjmjclbqbeigjqelcrfmzrvkbvnbbxcdovqzxruhvsaphrezinelmlbgsijrcyjgpeuoejxxlzuvbveckptjgycjevlosohezumzpjqjfzzzsnudmyyyrnmdgpkbqusabvyzhnbzsdvqczmkrbllrcjcdvifbhfojlqvfrstuvpqseabnaodfmgyhcyoessbhacajjllqyfyynpmbyhfiofetpykmmlgkycfqxhjcayirrnnmgbgfiqcuzitqnxmkskqklozdkjgpccmrkgthaocuegduejhpcsrebfgxfefuvxifhktzjvhkvloljatzaniccheoblzjjzjsmisedetigfsfcjhsygfmbvpgbvrbriupdsiyrmitzuqcosrzfcubnasocfapmulyhnucjjamoqqlsgqsofleiaeykunohboksgobpudqydnpjpprguqcangmifqbcyvrnpbtociosoesxknnibnqmxbhbjihqfnpluubezfnqgqrsehxbvrmhqdvxponoobobafdcmtulomlqqgjpkpqqhfsuicckodgtrcfmsyyloiaopcmtgbvtlnvmjpbiggygzdfrvitlrjmiskablertnixsloiicvykdcvebpmupxdmctmztbpxhgppyrlhlnmvnpfpodfdavhbuodfxtxialdcfcdzddeehbfookscmehdqrmvuiaspajrzyzxlaqfhrmrjhsejndyrkavkohfxobknichuomfkhgahtnnoizzoohjcatgnenzxdolq'
            ), 13)
        self.assertEqual(
            solution.substringDiff(
                7,
                'sxyrzxdclzhlkvpaxxyobkjkvchzskbfbxjtfivxibkznfsiybpzxhbylgpkdrfcqjtfovlizjtojkkqaibgmtrarayagcjiayzcdqgkuymlsdqzyvgokaxbfhfkrthcvmhuhdgyqbsnmdaonojiupshltcqpdxfoecjjigdgrmhrijjbjzuemnqbjjiooyjgurekokzomuvsxcbrvmjuvfbnrblkvozcflaafxfrynrlypzksadoujgbxbcgcoirvpjfyhjvxorynkyrqhemaeixujzscezpdakbpnuhcfabggqkmtclbmpuivuarzgfocigbhpxrrbatrrcuuamexerkfvajksfhuktntmrflbinhccivrzsmnepeajcvytajdndaktrqhaeihemgroxsratzyvvszcauqvgbbmtxqizttnidvfmaihtmtavtprstngqynismgjnbikgigvrmtgyidsachybpdglkztjniexelhyjqdmyxrjeoymuoxojsvfiakbtfnmexdruzzeygorinzbopvjefasoaaggvrskhoqmjqcuuivqmxhlxdpndamqegqvpkhbhrdylidczpxdslxxchfjuzeymgztsrkryctfrkqnnbtpiodhahqajtxmlracneiabysftvvpxaclbhuygvrcajrguznbolvdmxgudxsdbnfnrzvbenrifepkaqunyoyxzcrfexpqgqhklrzbqdfuffmxozaofuslomevvbvguxjorbjljghsvmfjfovhbptuxefjrxtiuqipcqdalvvxatbiyqafzjpqcqdhulkyiiqujpjlzlzhusutgnsausvvvdfyfiqiikspvmjerssspdjepjeaonnncckvhzdumnqqyvxygixczuhxpljyzdibjpantqzrpdvrgtfvlpxilrjrulxnotknfxqduyhtsiqoxkodsgqarzxvxurcqsklxidlfqjedrujariydryrvtxmqzglxpetuigvjvfgmbmdccyaqmkkjvlvylbakknrihbzqgfpnsdscymviuhidjxzxrafggiedznmlvrshtxepsznntdciuduojqramuidoxxnbotoedskucqhnddzrdxnookcszoienxkghbxqpmaofipsyuzrmktspoalyoxvslarqlzvmppkkfpuslbcpqefmsdjxgebtgzipicovctqhuvrggrhtyqptacncldxxptaxmaauphxchbklinisaixafdrzgakugmsmfqugoplqodbdefqisypsmfhtmcxdmbtsxpclmojydzrattgzkuotcqtkblkudpndayurnyancoyepjlzposzyspnnrkffgqbnzkimsvzxbueozmxahhqpgijyzoxlkyicjfcfzrkxzssxzgszvagumautiandlryqslbmanhupnmqfuvbrghisjmmsrjrsqzixhiszdbmitxznochbctbkozxhebftnexhrgxd',
                'sxymzxdclzhlkvpaxxyobkjkvchzskbfbxjtfivxibknnfsiobpzxhdylgpkprfcrjtfovliujtojkkqaibgmtraraaaqcjiayzcdqgkujmlsdqzyvgokaxbfhfkrtuovmhuhdgyqbsnpdaonujiufshztcqpdxfoegjjibdgbmhrijjbjzuemnqbjjiooyxgurrkokzomuvsxcbrvmjuvfbnrblkvozcflaafxfrynrlypzksadoujybxbcgcoirvpjfyhjvxorynkyrqhemaeixujzscmzpdakbpnuhcfabggqkmtclbmpuivuarzgfofigbhpxrrbatrrcuuamexjrkfvajksfhuktnfzrflbinhccmvresmnepeajcvyvajdndakxrqhaeihemgroxsratzmvvozcauqvgbbmdxqizttnidvfsayhtmtavthrntngqynismgjnbikgigvrmtgyidgachybpdglkitjniexelhyjqdmyxrjeotmuoxojsvfiakbtfnmexdruzzeygorinzivpvjefasnaaggvrskhoqmjqcuuivqmxhlxdpndamqegqvpkhuhrdylidczpgdslxxchfjuzeymgztsekrycufrsqnnbtpioihahqajnxmurycneiabysftuvpxaclbhuygvrcajrguznbolrdmxgudxsdbnfnrzvbedriybpkaqunyogxzcrfexpqgmhklrzbqdfuffmxozaofuslnmevvbvgqxjorbjljghvvmxjfovsbptuxefjdxtiuqimcqdalvvxatbyyhafzjvqcpdhulkyiiqujpjlvlvhusutgnsausvvvdfyfiqiikspvmjersssrdjepjeaonnncckvhadumnqqyvxygixczuhxpljyzdtbjpantqzrpdvrgbfvlpxilrjrulxnotknfxqduzhtyiqoxkoosgqaozdvxurcqskldidlfqjedrujariydryrvtxmqzgnxpetuigvhvfgmbmdccyaqmkojvlvylbakknaipbzmgfpnsdscymviumidjizxrafkgiedznmlrrshtvepsznntdciusiojqrqmuidoxxnbotoedbkucqhnjdzrsxnookcszoienxkghbxqpmaofipsyulrmktspoalyoxvslirrlzvmppkkfpuslbcpqefmsdjxgebtgzipicovctqhuvrggrhtysptrcncldxxptaxmaauphxchbklinisaixafdrzoakugmsmfqggoplqodbdefqisypsmfhtmcxdmbtsxpclmojydzrattgzkuodcqtkblkudpndayuretancoygpjlzloszyspnnrkffgqbnzkimsvzxbueozmxahhqpgijyzoxluyicjfcfzrkfzssxzgszvagumaxtianylryqslbmanhupbmqfevbrghisjmmsrjrsqzijhkszdbmitxhnochbctbkozxhebstnexhrgxd'
            ), 195)
        self.assertEqual(
            solution.substringDiff(
                520,
                'lkurxpqjflnelzqcexamlabkriugdnzidtcnmzoytfstqnotcsgrjsyknamhbikojrqihdrihslllhrizfjmnsxgedfixmprmijbirlsoputtuivgvmhjzendeflrvshvrkueshztcivyucaysltufblxndbgmrfdidbugityspupcpcmfayferabyujzzmqdzntzxxtxvrxvycsntqadynvirofnupnphcjhiuhgbpbyrkytrcartekluefmjyqollpsjacjtfitluvkmlodosxefzivcnvcxkiyelpilancximvdtjhmcpdqhalfixbxysbzvuiiyzkmjfnpekpqqrcecgfbnpehyholkgylrkdixytzhhucrpmskeazuzckhgdivrnpycqffcqiivztgtjgmgjoccjecvdkztsskgofctcxuqevazpbmouemdasgjbyecelnonnnkvgfjcptusqiovlagkofubshlxitfjmcfggbltaobyhiajgojtktqdojksjyzpsaayosvhginokqbhmrcbgxjkyntecjrefexxtpymjdpacusxfodocdlybdfidhkhyrcadsiqhildusucpslterupctbbkfyyfrhrloqklafstzhfdjknmhifmcftybbtcvgiqknmegztizopjtrzgzhlbjczihjdebgjzyntckmaehladvehpejphajhpccjkjobjyypeyociscvipyhbvgvbdjkybhjpdazvalifhrdlferncgbpjlgouukppirrfnvddbgaxxytxbybvmfcgzxnimgyujqanmkhazmdpyvkftqqvemptocyuydzrxmstzhqhbsobtkltxpfkhfltyrteqqxdzshuxglrndyhnigooojdekczeomoyermnuajqcnhxqjkriabiesqhnpsdoycqqripzjolcgbpionldmqxqehmntxjfflyrtyvlkfitgbjtrqxibujmdcvjnsvlmjqjbhqfrlhblupmttxkpmoxumehhamhmyljvfaxcfjnuasrlzeladjygaofqyovjxeapkknouqqdiadsznhgnjnhpzdukdrujbtjajdksyvdmmostxuhqxgphrsnorijxypjvcgdkueyhpajybhfblhnhijnnrsxiycekmsmautlgqykjaupdvtnjdmqyjmbrxphsmfsqvedadnfkhgildavuimqxinaaohkhccqcbokqcdcgjjnrncometlciasunfoblgtdxuetjarzyglcjxelajojnomexfbfsaiqbtrprsjlcurgoiaommbumsyudctrttdzdczpnsinufkikyrjujruxrrbkfllxejedcsistkzvkvsivcevzlebzdxvdzkbxcfnszlrzfjypaumamypoqvbsudzniooaryhknlslfbjtfjpnfqlbehporyhbirjrydjepiprkxuiocsgdzaglokvvgyejrsqequyveoeaamnolm',
                'lkurxpfjflnelrqcexamlabkriugdnzidtclmzoytfstqnotcsgrjsyknamhbikojrqihdrihslllhhizfjmnsxgedfixmprmijbirlsoputtuivgvmhjzendeflrvshvrkueshztcivyucaysltufblxndbgmrfdidbugityspupcpcmfayferabyujzzmqdzntzxxtxvrxvycsntqamynvirofnupnphcjhiuhgbpbyrkktrgartekluefmjyqollpsjacjtfitluvkmlodosxefzivcnvcxkiyelpilancximvdtjbmcpdqhaefixbxysbzvuiiyzkmjfnpekpqqroecgfbnpelyholkcylrkdixytzhhucrpmskeazuzckhgdivrnsycqffcqiivztgtjgmgjoccjecvdhztsskgofctcxuqevazpbmouemdasgjbyecelnonnnkvgfjcptusqiovlmgkofubshlxitfjmcfggbltaobyhiajgojtktqdojksjyzpsaayosvhginokqbhmrcbgxjkyntecjrefexxtpypjdpactsxfodgcdlybdfidhkyyrcadsiqhildusucusfterupctbykfyyfrhrlouklafstrhfdjknmhifmcfdybbtcvgiqknmegztizopjtrzgzhlbjczixjdebxjzyntckmaesladvehpejphajhpccjkjobjcypeyociscvipyhbsgvbdjkybhjpdazvasifhrdlfeancgbpjlgouukppirrfcvudbgaxxytxbybvmfcgzxnimgyujqanmkhazmdpyvkftqqvemptocyuydzrxmstzhqhbsobtkltxpfkhfltyrtmqqxdzshuxglrndyhnigooojdekczeomoyermnuajqcnhxqjkrfabiesqhnpsdoycqqripzvolcgbpionldmqxqehnmmxjfflyatyvlkfitabjtrqxibujvdcejnsvlmjqjbhlfrlhblupmttxkpmoxumehhamhmyljvfaxcfjnuasrlzeladjygaofqyovjxeapkknouqqdiadsznhgnjnhpzdukdrujbtjajdksyvdmmqstxuhqxgphmsnorpjxypjvcgdkueyhpajybhfblhnhijnnrsxiycekmsmautlgqykjaupdvtnjdmqyjmbrxhhsmfsqvedadnfkhgildavuiaqxinraohkhccqcbokqcdcgjjnrncfmeelciasunfoblgtdruetjarzyglaaselajojnomexfbfsaiqbtrhrsjlcurgoiaommbumsyudctkttdzdczpnsinufkikyrjujruxrrbkfllxejedcsistkzvkvsivcevzlebzdxvdzkbxcfnsdlrzfjypaimamypoqvbsudzniooaryhknlslfbjtfjpnfqlbehpohyhbirjrydjepiprkxuiocsgdzaglokvvgyejrsqequlveoeaamnolm'
            ), 1500)


if __name__ == '__main__':
    unittest.main()