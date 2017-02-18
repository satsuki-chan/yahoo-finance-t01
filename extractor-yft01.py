#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
from time import sleep
from simplejson import JSONDecodeError
from yahoo_finance import Share

def validate(date_text):
   try:
      datetime.datetime.strptime(date_text, '%Y-%m-%d')
      return True
   except ValueError:
      return False


cdate = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
# [2016-02-20] - Modification to search from a specific date: '2015-11-28'
#n_found_data = "found_data_{}.csv".format(cdate)
#n_found_error = "found_error_{}.txt".format(cdate)
n_found_data = "found_data_extra_{}.csv".format(cdate)
n_found_error = "found_error_extra_{}.txt".format(cdate)
# [2016-02-20] -
print cdate + ": {} - {}".format(n_found_data, n_found_error)
# [2016-02-20] - Modification to search from a specific date: '2015-11-28'
#hend_date = '2015-11-27'
hend_date = '2015-12-31'
# [2016-02-20] -
found_data = open(n_found_data, "w")
found_error = open(n_found_error, "w")

list_founds = [
    ['ACCIPAT B0-B', '1987-12-08'],
    ['ACCIPAT C0-B', '2009-09-07'],
    ['ACTICRE B', '1994-12-22'],
    ['ACTICRE FF', '2008-06-13'],
    ['ACTINTK FF', '2003-12-01'],
    ['ACTIPAT B', '1994-12-16'],
    ['ACTIPAT FF', '2008-01-18'],
    ['ACTIVAR B', '1997-07-09'],
    ['ACTIVAR FF', '2008-04-07'],
    ['B+RV F', '2010-12-14'],
    ['B+RV GB', '2010-12-14'],
    ['B+RV NC', '2010-12-14'],
    ['B+RV P', '2010-12-14'],
    ['B+RV PV', '2010-12-14'],
    ['BMERCRE GB', '2008-05-15'],
    ['BMERCRE MB', '2008-05-15'],
    ['BMERCRE NC', '2010-08-02'],
    ['BMERIND F', '2004-11-24'],
    ['BMERIND GB', '2008-05-07'],
    ['BMERIND MB', '2006-07-10'],
    ['BMERIND P', '2006-07-10'],
    ['BMERIND PV', '2006-07-10'],
    ['BMERPAT B', '1989-05-19'],
    ['BMERPAT F', '2004-11-24'],
    ['BMERPAT GB', '2008-05-14'],
    ['BMERPAT P', '2010-02-25'],
    ['BMERPAT PV', '2010-02-25'],
    ['BNMPAT B2-A', '2007-10-15'],
    ['BNMPAT B3-A', '2010-11-30'],
    ['BNMPAT C0-A', '2010-08-26'],
    ['BNMPAT C0-C', '2007-10-15'],
    ['BNMPAT M0-A', '2010-11-26'],
    ['CRECE+ B-1', '2008-02-15'],
    ['CRECE+ B-2', '2008-02-15'],
    ['CRECE+ B-E', '2010-12-30'],
    ['DIVER-A B', '2004-11-26'],
    ['DIVER-A GB', '2010-01-11'],
    ['DIVER-C GB', '2010-03-04'],
    ['DIVER-C MB', '2010-03-04'],
    ['DIVER-M B', '2004-11-26'],
    ['DIVER-M GB', '2010-03-12'],
    ['ELITE-C B1', '2009-07-06'],
    ['ELITE-M B1', '1998-05-27'],
#    ['F-BOLSA B', '2000-12-01'],
#    ['F-INDIC B', '2000-12-01'],
    ['FONBNM B3-A', '1990-11-14'],
    ['FONBNM C0-A', '2010-08-26'],
    ['FONBNM C0-C', '2007-02-06'],
    ['FONBNM C0-D', '2009-02-09'],
    ['FONBNM C1-A', '2009-02-09'],
    ['FONBNM C3-A', '2007-02-06'],
    ['FONBNM M0-A', '2009-02-09'],
    ['FONDOM2 B', '2006-02-21'],
    ['FONIBUR B', '1987-11-30'],
    ['GBMAAA BO', '1994-11-24'],
    ['GBMAGR B', '2007-08-10'],
    ['GBMCRE BD', '2010-12-22'],
    ['GBMCRE BO', '2000-01-03'],
    ['GBMINF BO', '2008-09-01'],
    ['GBMIPC BO', '1992-03-23'],
    ['GBMMOD BO', '2005-08-08'],
    ['GBMPAGR B', '2010-05-19'],
    ['GBMPCON B', '2010-07-23'],
    ['GBMPMOD B', '2010-05-19'],
    ['GBMV1 BO', '1987-08-07'],
    ['GOLD3+ B1-C', '2009-03-18'],
#    ['GOLD3+ B2-A', '2008-11-05'],
#    ['GOLD4+ B2-B', '2003-09-01'],
#    ['GOLD5+ B2-C', '2008-11-05'],
    ['HSBC-F2 BFP', '2006-02-28'],
    ['HSBC-F2 BFV', '2006-02-28'],
    ['HSBC-F3 BFA', '2007-09-04'],
    ['HSBC-F3 BFP', '2007-09-04'],
    ['HSBC-F3 BFS', '2005-09-02'],
    ['HSBC-F3 BFV', '2007-08-28'],
    ['HSBC-RV BFA', '2004-06-01'],
    ['HSBC-RV BFP', '1983-03-15'],
    ['HSBC-RV BFS', '2004-06-01'],
    ['HSBC-RV BFV', '2004-06-01'],
    ['HSBC-RV BNF', '2007-08-27'],
    ['HSBCBOL BFA', '2004-06-01'],
    ['HSBCBOL BFP', '2004-06-01'],
    ['HSBCBOL BFS', '2004-06-01'],
    ['HSBCBOL BFV', '2004-06-01'],
    ['HSBCBOL BNF', '2007-08-27'],
    ['IBUPLUS B', '2004-09-17'],
    ['INBURSA B-3', '1990-04-01'],
    ['INTEC B', '2010-01-14'],
    ['INTERDV B', '2008-02-01'],
    ['INVEXMX BE', '2009-07-02'],
    ['INVEXMX BMF', '1998-04-17'],
    ['ISOLIDO B', '1989-07-12'],
    ['IXE1 BI', '2008-05-08'],
    ['IXE1 F2', '2008-05-08'],
    ['IXE1 F3', '2008-05-08'],
    ['IXE1 I2', '2010-07-09'],
    ['IXE1 I3', '2010-12-31'],
    ['IXE2 BI', '2008-05-08'],
    ['IXE2 F2', '2008-05-08'],
    ['IXE2 F3', '2008-05-08'],
    ['IXE2 I2', '2008-05-08'],
    ['IXE3 BI', '2008-05-08'],
    ['IXE3 F2', '2008-05-08'],
    ['IXE3 F3', '2008-05-08'],
    ['IXE3 I2', '2010-07-09'],
    ['IXE3 I3', '2009-11-09'],
    ['IXECON API-F', '2008-04-09'],
    ['IXECON BI', '2008-04-09'],
    ['IXECON BS', '2007-04-13'],
    ['IXECON F1', '2008-04-09'],
    ['IXECON F2', '2008-04-09'],
    ['IXEESP BF1', '2010-01-22'],
    ['IXEESP BF2', '2010-01-22'],
    ['IXEESP BI', '2010-01-22'],
    ['MAYA B1', '2010-02-23'],
    ['MAYA B2', '2010-02-25'],
    ['MAYA B3', '2010-02-25'],
    ['MAYA D', '2010-03-05'],
    ['MIFIPC B', '1999-08-23'],
    ['MONEXCR BEC-1', '2007-06-22'],
    ['MONEXCR BFC-1', '2007-06-22'],
    ['MONEXCR BFC-2', '2007-06-22'],
    ['MONEXCR BFC-3', '2007-06-22'],
    ['MONEXCR BFD', '2010-06-21'],
    ['MULTIPC B', '2000-10-06'],
    ['NAFINDX F1', '2010-07-06'],
#    ['NTE+EMP F1', '2004-05-04'],
    ['NTE+EMP I1', '2010-02-03'],
#    ['NTE+IN F1', '1997-08-04'],
#    ['NTE+IN I1', '2007-12-03'],
#    ['NTE+SEL F', '2006-07-24'],
#    ['NTE+SEL F1', '2006-07-24'],
    ['NUMC B0-B', '1999-09-09'],
    ['NUMRV B0-A', '2006-02-07'],
    ['NUMRV B3-A', '1987-10-29'],
    ['NUMRV C0-A', '2009-07-06'],
    ['OM-RVMX B', '2004-05-18'],
    ['OM-RVMX E', '2010-10-13'],
    ['PRINLS2 FA', '2008-08-07'],
    ['PRINLS2 FB', '2008-08-08'],
    ['PRINLS2 FC', '2009-07-09'],
    ['PRINLS2 XC', '2010-09-06'],
    ['PRINLS3 FA', '2008-08-04'],
    ['PRINLS3 FB', '2008-08-05'],
    ['PRINLS3 FC', '2009-07-09'],
    ['PRINLS3 XC', '2010-03-26'],
    ['PRINRVA FA', '2007-10-12'],
    ['PRINRVA FB', '2007-10-12'],
    ['PRINRVA FC', '2007-10-12'],
    ['PRINRVA FF', '2007-10-12'],
    ['PRINRVA XB', '2007-10-12'],
    ['PRINRVA XC', '2010-12-07'],
    ['PROF-1A B', '2010-11-17'],
    ['PROF-3A B', '2009-12-15'],
    ['SBMIX B', '1987-09-08'],
    ['SCOT-RV L', '2009-01-22'],
    ['SCOTIPC L', '1987-09-23'],
    ['SCOTIPC TF', '2006-03-13'],
    ['SELECTC B1', '2009-07-06'],
    ['SELECTD B1', '1989-03-17'],
#    ['ST&ER-D B1', '1983-06-06'],
#    ['ST&ER-I B1', '1990-02-16'],
#    ['ST&ER-I F', '2009-08-13'],
#    ['ST&ERBM F', '2007-07-31'],
    ['STER-GR B', '1995-11-13'],
    ['STER-OP B1', '2005-11-18'],
    ['SURIPC BDF', '2001-10-10'],
    ['SURIPC BF', '2010-04-07'],
    ['SURIPC BOE2', '2010-04-07'],
    ['SURIPC BOE4', '2010-04-07'],
    ['SURPAT BDF', '2006-04-27'],
    ['SURPAT BOE1', '2006-04-27'],
    ['SURPAT BOE2', '2006-04-27'],
    ['SVIVE20 B', '1984-12-27'],
    ['SVIVE20 S', '2010-04-16'],
    ['SVIVE35 S', '2010-04-16'],
    ['SVIVE50 S', '2010-04-16'],
    ['VALMX20 B0', '1996-08-27'],
    ['VALMX20 B1', '2004-01-15'],
    ['VALMX20 B2', '2004-01-15'],
    ['VALMX24 B0', '2005-09-01'],
    ['VALMX24 B1', '1986-12-03'],
    ['VALMXA B0', '2005-09-30'],
    ['VALMXA B1', '2005-09-30'],
    ['VALMXA B2', '2005-09-30'],
    ['VALMXB B0', '2005-09-30'],
    ['VALMXB B1', '2005-09-30'],
    ['VALMXB B2', '2005-09-30'],
    ['VALMXC B0', '2005-09-30'],
    ['VALMXC B1', '2005-09-30'],
    ['VALMXC B2', '2005-09-30'],
    ['VALUEV6 B', '2000-10-06'],
    ['VECTCR F', '1997-01-02'],
    ['VECTCR X', '1997-01-02'],
    ['VECTIND F', '1998-06-29'],
    ['VECTIND X', '2006-01-02'],
    ['VECTPA F', '1997-01-02']
]

# print list_founds
for cfound in list_founds:
    name_found1 = cfound[0].replace('+', '').replace('.', '').replace(' ', '').replace('&','%26').replace('-', '') + ".MX"
    name_found2 = cfound[0].replace('+', '').replace('.', '').replace(' ', '').replace('&','%26') + ".MX"
    hdata_found = 0
    list_nfounds = list()
    list_nfounds.append(name_found1)
    if name_found1 != name_found2:
        list_nfounds.append(name_found2)
    print '{0} ({1}): "{2}"'.format(cfound[0], cfound[1], list_nfounds)

    for name_found in list_nfounds:
        try:
            ofound = Share(name_found) # Found object
            sleep(1) # Pause time (1 segs.) to avoid server rejections
            try:
                info = ofound.get_info()
                print info

                if info.get('start') == None:
                    found_error.write("-Error-[{}]: No 'start' and 'end' dates for historical data. Used code: '{}'\n".format(cfound[0], name_found))
                #elif not validate(info['start']):
                #    found_error.write("-Error-[{}]: No valid 'start' date for historical data. Used code: '{}', fault date: '{}'\n".format(cfound[0], name_found, info['start']))
                else:
                    if not validate(info['start']):
                    # [2016-02-20] - Modification to search from a specific date: '2015-11-28'
                    #    found_error.write("Warning[{}]: No valid 'start' date for historical data. Used code: '{}', fault date: '{}', substitute date: '{}'\n".format(cfound[0], name_found, info['start'], info['start'].replace('-NaN-', '-01-')))
                    #    info['start'] = info['start'].replace('-NaN-', '-01-')
                    #    if validate(info['start']):
                    #        print "   ---> 'start': '{}'".format(info['start'])
                    #sdate = datetime.datetime.strptime(info['start'], '%Y-%m-%d')
                    #idate = datetime.datetime.strptime(cfound[1], '%Y-%m-%d')
                    #if idate <= sdate:
                    #    hstart_date = cfound[1]
                    #else:
                    #    hstart_date = info['start']
                        found_error.write("Warning[{}]: No valid 'start' date for historical data. Used code: '{}', fault date: '{}', default start date: '2015-11-27'\n".format(cfound[0], name_found, info['start']))
                    hstart_date = '2015-11-27'
                    # [2016-02-20] -
                    sleep(1) # Pause time (1 segs.) to avoid server rejections
                    try:
                        #hdata = ofound.get_historical(info['start'], hend_date)
                        hdata = ofound.get_historical(hstart_date, hend_date)
                        print "   - start_date: '{}', end_date: '{}'".format(hstart_date, hend_date)
                        #print hdata
                        for hday in hdata:
                            if hday.get('Date') == None:
                                found_error.write("-Error-[{}]: No valid historical record. Used code: '{}', raw record: \"{}\"\n".format(cfound[0], name_found, hday))
                            else:
                                #print '"{}", "{}", {}'.format(cfound[0], hday['Date'], hday['Close'])
                                found_data.write('"{}","{}",{}\n'.format(cfound[0], hday['Date'], hday['Close']))
                        hdata_found += 1
                        found_data.flush()
                        os.fsync(found_data.fileno())
                    except JSONDecodeError:
                        found_error.write("-Error-[{}]: Network failure while retriving historical records. Used code: '{}'\n".format(cfound[0], name_found))
                        pass
            except JSONDecodeError:
                found_error.write("-Error-[{}]: Network failure while retriving found information. Used code: '{}'\n".format(cfound[0], name_found))
                pass
        except JSONDecodeError:
            found_error.write("-Error-[{}]: Network failure while creating found object. Used code: '{}'\n".format(cfound[0], name_found))
            pass

        hday = None
        hdata = None
        info = None
        ofound = None
        sleep(3) # Pause time (3 segs.) to avoid server rejections

    if hdata_found == 0:
        found_error.write("Warning[{}]: No historical data found with any code.\n".format(cfound[0]))
    elif hdata_found >= 2:
        found_error.write("Warning[{}]: TWO or more sets of historical data found with all codes.\n".format(cfound[0]))

    found_error.flush()
    os.fsync(found_error.fileno())
    sleep(5) # Pause time (5 segs.) to avoid server rejections

found_data.close()
found_error.close()
