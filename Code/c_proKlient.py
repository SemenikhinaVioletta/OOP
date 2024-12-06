import c_Class_Pro_Klient as Pro
import f_Class_status_klient as stat

sta = stat.status_Klient(1, "Bad")
klient = Pro.Pro_Klient(1, "V V V", 98773232232, 0, [1, 2, 3], "qw@qw.sd", 1, None)
klient.enter_klient_to_bd()


def do_pro_klient(flag, wind):
    pass