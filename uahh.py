import random

class Useragent:
    def __init__(self):
        self.versi_ig = f'{str(random.randint(100, 380))}.0.0.{str(random.randint(10, 60))}.{str(random.randint(90, 220))}'
        self.versi_andro = random.choice([
            "27/9", "27/10", "27/11", "27/12", "27/12", "27/13", "28/9", "28/10", "28/11", "28/12", "28/12",
            "28/13", "29/9", "29/10", "29/11", "29/12", "29/12", "29/13", "27/9", "30/10", "30/11", "30/12",
            "30/12", "30/13", "31/9", "31/10", "31/11", "31/12", "31/12", "31/13", "32/9", "32/10", "32/11",
            "32/12", "32/12", "32/13", "33/9", "33/10", "33/11", "33/12", "33/12", "33/13", "32/26", "34/26",
            "32/11", "34/12", "30/10", "34/12.0.1", "30/11.0.3"
        ])
        self.versi_ios = random.choice(['9_2','9_2_1','9_3','9_3_1','9_3_2','9_3_3','9_3_5','10_0_2','10_1_1','10_2','10_2_1','10_3_1','10_3_2','10_3_3','11_2','11_1','11_1_1','15_6','11_1_3','11_3_2','11_2_1','11_2','13_2_1','14_2_1','15_1_1','12_1_1','12_1','12_1_2','12_2_1','16_1','16_2','13_3','13_1_1','13_2_1','14_3_5','9_1','8_1','7_1','10_1','9_1_1','8_1_1','9_2_1','8_2_2','15_3_2','15_4','14_3','13_5','14_5','13_4','16_5_1','16_0','16_1','16_1_2','16_0_1','16_0_3','16_3_1','16_4_1','16_2','16_4','16_5','16_6','16_6_1','17_0','17_3_1','17_4_1'])
        self.iph = random.choice(['2.00','3.00'])
        self.versi_iphone = random.choice(['4,1','6,1','6,2','7,2','8,4','10,4','10,5','11,8','14,2','14,3','14,5','15,1','16,1'])

    def ua_api(self):
        self.oppo = random.choice([
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 480dpi; 1080x2161; OPPO; CPH2109; OP4BA5L1; qcom; id_ID; 289692198)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 360dpi; 720x1445; OPPO; CPH2637; OP4F2F; mt6765; id_ID; 337202351)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 480dpi; 1080x1920; samsung; SM-A520F; a5y17lte; samsungexynos7880; id_ID; 99640911)',
            f'Instagram {self.versi_ig} (iPhone{self.versi_iphone}; iOS {self.versi_ios}; id_ID; id_ID; scale={self.iph}; gamut=normal; 750x1334)'
        ])
        self.kintil = random.choice([
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 640dpi; 1440x2560; vivo; vivo Xplay5S; PD1516A; qcom; id_ID; 99640911)'
            f'Instagram {self.versi_ig} (iPhone{self.versi_iphone}; iOS {self.versi_ios}; id_ID; id_ID; scale={self.iph}; gamut=normal; 750x1334)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 1344x720; Xiaomi; Redmi 5; rosy; qcom; id_ID; 99640905)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 320dpi; 720x1280; Xiaomi; Redmi Note 5; redfin; qcom; id_ID)'
        ])
        self.mekimamak = random.choice([
            f'Instagram {self.versi_ig} (iPhone{self.versi_iphone}; iOS {self.versi_ios}; id_ID; id_ID; scale={self.iph}; gamut=normal; 750x1334)',
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 420dpi; 1080x2340; samsung; SM-G973F; beyond1; exynos9820; id_ID)',
            f'Mozilla/5.0 (iPhone; CPU iPhone OS {self.versi_ios} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram {self.versi_ig}'
            f'Instagram {self.versi_ig} Android ({self.versi_andro}; 420dpi; 1080x2340; samsung; SM-G991B; o1s; exynos2100; id_ID)'
        ])
        self.CROOT = random.choice([self.mekimamak, self.kintil, self.oppo])
        return self.CROOT