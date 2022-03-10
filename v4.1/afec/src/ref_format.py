from datetime import datetime
import connectserver

db = connectserver.connectserver()
cursor = db.cursor()

class format:
    default = {}
    racecalendar = {}
    driverformat = {}
    teamformat = {}
    pointsformat = {}
    licensepointformat = {}
    groupformat = {}
    lanusernameformat = {}
    raceresultformat = {}
    racedirector = {}

    def __init__(this, workbook):
        this.workbook = workbook

        # default format
        # for driver list
        groupf = workbook.add_format({"font_size":12})
        groupf.set_font_name("Dengxian")
        groupf.set_align("center")
        groupf.set_align("vcenter")
        this.default["groupf"] = groupf
        reservef = workbook.add_format({"font_size":11})
        reservef.set_font_name("Dengxian")
        reservef.set_align("vcenter")
        this.default["Reserve"] = reservef
        testingf = workbook.add_format({"font_size":11})
        testingf.set_font_name("Dengxian")
        testingf.set_bg_color("#00CC00")
        testingf.set_align("vcenter")
        this.default["Testing"] = testingf
        failtestingf = workbook.add_format({"font_size":11})
        failtestingf.set_font_name("Dengxian")
        failtestingf.set_bg_color("#974706")
        failtestingf.set_align("vcenter")
        this.default["Failed"] = failtestingf
        retiredf = workbook.add_format({"font_size":11})
        retiredf.set_font_name("Dengxian")
        retiredf.set_bg_color("#000000")
        retiredf.set_font_color("#FFFFFF")
        retiredf.set_align("vcenter")
        this.default["Retired"] = retiredf





        # race calendar format
        # race header format
        RCHformat = workbook.add_format({"font_size":26})
        RCHformat.set_font_name("Dengxian")
        RCHformat.set_bold(True)
        RCHformat.set_align("center")
        RCHformat.set_align("vcenter")
        this.racecalendar["RCHformat"] = RCHformat
        # small header format
        RCdefaultf = workbook.add_format({"font_size":16})
        RCdefaultf.set_font_name("黑体")
        RCdefaultf.set_align("center")
        RCdefaultf.set_align("vcenter")
        this.racecalendar["RCdefaultf"] = RCdefaultf
        # race TO BE GO format
        racetobegof = workbook.add_format({"num_format": "yyyy/m/dd"})
        racetobegof.set_font_size("16")
        racetobegof.set_font_name("黑体")
        racetobegof.set_align("center")
        racetobegof.set_align("vcenter")
        this.racecalendar["TO BE GO"] = racetobegof
        # race FINISHED format
        racefinishf = workbook.add_format({"num_format": "yyyy/m/dd"})
        racefinishf.set_font_size("16")
        racefinishf.set_font_name("黑体")
        racefinishf.set_align("center")
        racefinishf.set_align("vcenter")
        racefinishf.set_bg_color("#00FF00")
        this.racecalendar["FINISHED"] = racefinishf
        # race CANCELLED format
        racecancelf = workbook.add_format({"num_format": "yyyy/m/dd"})
        racecancelf.set_font_size("16")
        racecancelf.set_font_name("黑体")
        racecancelf.set_align("center")
        racecancelf.set_align("vcenter")
        racecancelf.set_bg_color("#000000")
        racecancelf.set_font_color("#FFFFFF")
        this.racecalendar["CANCELLED"] = racecancelf
        # race ON GOING format
        raceongoingf = workbook.add_format({"num_format": "yyyy/m/dd"})
        raceongoingf.set_font_size("16")
        raceongoingf.set_font_name("黑体")
        raceongoingf.set_align("center")
        raceongoingf.set_align("vcenter")
        raceongoingf.set_bg_color("#3399FF")
        this.racecalendar["ON GOING"] = raceongoingf
        # SEASON BREAK format
        seasonbreakf = workbook.add_format({"num_format": "yyyy/m/dd"})
        seasonbreakf.set_font_size("16")
        seasonbreakf.set_font_name("黑体")
        seasonbreakf.set_align("center")
        seasonbreakf.set_align("vcenter")
        seasonbreakf.set_bg_color("#FFFF00")
        this.racecalendar["SEASON BREAK"] = seasonbreakf
        
        
        
        
        
        

        # driver format
        redf = workbook.add_format({"font_size":11})
        redf.set_bg_color("#FF0000")
        redf.set_font_name("Dengxian")
        redf.set_align("vcenter")
        this.driverformat["Red"] = redf

        greenf = workbook.add_format({"font_size":11})
        greenf.set_bg_color("#00FF00")
        greenf.set_font_name("Dengxian")
        greenf.set_align("vcenter")
        this.driverformat["Green"] = greenf

        bluef = workbook.add_format({"font_size":11})
        bluef.set_bg_color("#0066CC")
        bluef.set_font_name("Dengxian")
        bluef.set_align("vcenter")
        this.driverformat["Blue"] = bluef

        yellowf = workbook.add_format({"font_size":11})
        yellowf.set_bg_color("#FFFF00")
        yellowf.set_font_name("Dengxian")
        yellowf.set_align("vcenter")
        this.driverformat["Yellow"] = yellowf

        cyanf = workbook.add_format({"font_size":11})
        cyanf.set_bg_color("#00B0F0")
        cyanf.set_font_name("Dengxian")
        cyanf.set_align("vcenter")
        this.driverformat["Cyan"] = cyanf

        pinkf = workbook.add_format({"font_size":11})
        pinkf.set_bg_color("#FF66CC")
        pinkf.set_font_name("Dengxian")
        pinkf.set_align("vcenter")
        this.driverformat["Pink"] = pinkf

        sliverf = workbook.add_format({"font_size":11})
        sliverf.set_bg_color("#C0C0C0")
        sliverf.set_font_name("Dengxian")
        sliverf.set_align("vcenter")
        this.driverformat["Sliver"] = sliverf

        grayf = workbook.add_format({"font_size":11})
        grayf.set_bg_color("#808080")
        grayf.set_font_name("Dengxian")
        grayf.set_align("vcenter")
        this.driverformat["Gray"] = grayf

        purplef = workbook.add_format({"font_size":11})
        purplef.set_bg_color("#9900CC")
        purplef.set_font_name("Dengxian")
        purplef.set_align("vcenter")
        this.driverformat["Purple"] = purplef

        ooffff = workbook.add_format({"font_size":11})
        ooffff.set_bg_color("#00FFFF")
        ooffff.set_font_name("Dengxian")
        ooffff.set_align("vcenter")
        this.driverformat["#00FFFF"] = ooffff



        reservef = workbook.add_format({"font_size":11})
        reservef.set_font_name("Dengxian")
        reservef.set_align("vcenter")
        reservef.set_bg_color("#000000")
        reservef.set_font_color("#FFFFFF")
        this.driverformat["Reserve"] = reservef
        
        retiredf.set_font_name("Dengxian")
        retiredf.set_bg_color("#000000")
        retiredf.set_font_color("#FFFFFF")
        retiredf.set_align("vcenter")
        this.driverformat["Retired"] = retiredf





        # team format
        redf = workbook.add_format({"font_size":11})
        redf.set_bg_color("#FF0000")
        redf.set_font_name("Dengxian")
        redf.set_align("vcenter")
        redf.set_bold(True)
        this.teamformat["Red"] = redf

        greenf = workbook.add_format({"font_size":11})
        greenf.set_bg_color("#00FF00")
        greenf.set_font_name("Dengxian")
        greenf.set_align("vcenter")
        greenf.set_bold(True)
        this.teamformat["Green"] = greenf

        bluef = workbook.add_format({"font_size":11})
        bluef.set_bg_color("#0066CC")
        bluef.set_font_name("Dengxian")
        bluef.set_align("vcenter")
        bluef.set_bold(True)
        this.teamformat["Blue"] = bluef

        yellowf = workbook.add_format({"font_size":11})
        yellowf.set_bg_color("#FFFF00")
        yellowf.set_font_name("Dengxian")
        yellowf.set_align("vcenter")
        yellowf.set_bold(True)
        this.teamformat["Yellow"] = yellowf

        cyanf = workbook.add_format({"font_size":11})
        cyanf.set_bg_color("#00FFFF")
        cyanf.set_font_name("Dengxian")
        cyanf.set_align("vcenter")
        cyanf.set_bold(True)
        this.teamformat["Cyan"] = cyanf

        pinkf = workbook.add_format({"font_size":11})
        pinkf.set_bg_color("#FF00FF")
        pinkf.set_font_name("Dengxian")
        pinkf.set_align("vcenter")
        pinkf.set_bold(True)
        this.teamformat["Pink"] = pinkf

        sliverf = workbook.add_format({"font_size":11})
        sliverf.set_bg_color("#C0C0C0")
        sliverf.set_font_name("Dengxian")
        sliverf.set_align("vcenter")
        sliverf.set_bold(True)
        this.teamformat["Sliver"] = sliverf

        grayf = workbook.add_format({"font_size":11})
        grayf.set_bg_color("#808080")
        grayf.set_font_name("Dengxian")
        grayf.set_align("vcenter")
        grayf.set_bold(True)
        this.teamformat["Gray"] = grayf

        purplef = workbook.add_format({"font_size":11})
        purplef.set_bg_color("#6600CC")
        purplef.set_font_name("Dengxian")
        purplef.set_align("vcenter")
        purplef.set_bold(True)
        this.teamformat["Purple"] = purplef

        ooffff = workbook.add_format({"font_size":11})
        ooffff.set_bg_color("#00FFFF")
        ooffff.set_font_name("Dengxian")
        ooffff.set_align("vcenter")
        this.teamformat["#00FFFF"] = ooffff
        

        reservef = workbook.add_format({"font_size":11})
        reservef.set_font_name("Dengxian")
        reservef.set_align("vcenter")
        reservef.set_bg_color("#000000")
        reservef.set_font_color("#FFFFFF")
        reservef.set_bold(True)
        this.teamformat["Reserve"] = reservef
        
        




    
        # points format
        headerf = workbook.add_format({"font_size":11})
        headerf.set_font_name("Dengxian")
        headerf.set_align("center")
        headerf.set_align("vcenter")
        this.pointsformat["header"] = headerf
        p1 = workbook.add_format({"font_size":11})
        p1.set_font_name("Dengxian")
        p1.set_align("center")
        p1.set_align("vcenter")
        p1.set_bg_color("#FFFF00")
        this.pointsformat["p1"] = p1
        p2 = workbook.add_format({"font_size":11})
        p2.set_font_name("Dengxian")
        p2.set_align("center")
        p2.set_align("vcenter")
        p2.set_bg_color("#EEECE1")
        this.pointsformat["p2"] = p2
        p3 = workbook.add_format({"font_size":11})
        p3.set_font_name("Dengxian")
        p3.set_align("center")
        p3.set_align("vcenter")
        p3.set_bg_color("#FFC000")
        this.pointsformat["p3"] = p3
        points = workbook.add_format({"font_size":11})
        points.set_font_name("Dengxian")
        points.set_align("center")
        points.set_align("vcenter")
        points.set_bg_color("#00B050")
        this.pointsformat["points"] = points
        outpoint = workbook.add_format({"font_size":11})
        outpoint.set_font_name("Dengxian")
        outpoint.set_align("center")
        outpoint.set_align("vcenter")
        outpoint.set_bg_color("#538DD5")
        this.pointsformat["outpoint"] = outpoint
        retired = workbook.add_format({"font_size":11})
        retired.set_font_name("Dengxian")
        retired.set_align("center")
        retired.set_align("vcenter")
        retired.set_bg_color("#7030A0")
        this.pointsformat["retired"] = retired
        dns = workbook.add_format({"font_size":11})
        dns.set_font_name("Dengxian")
        dns.set_align("center")
        dns.set_align("vcenter")
        dns.set_bg_color("#A6A6A6")
        this.pointsformat["dns"] = dns
        dsq = workbook.add_format({"font_size":11})
        dsq.set_font_name("Dengxian")
        dsq.set_align("center")
        dsq.set_align("vcenter")
        dsq.set_bg_color("#FF0000")
        this.pointsformat["dsq"] = dsq
        dna = workbook.add_format({"font_size":11})
        dna.set_font_name("Dengxian")
        dna.set_align("center")
        dna.set_align("vcenter")
        this.pointsformat["dna"] = dna
    




        # license point format
        # excellent 11-12
        excellentf = workbook.add_format({"font_size":11})
        excellentf.set_font_name("Dengxian")
        excellentf.set_align("center")
        excellentf.set_align("vcenter")
        excellentf.set_bg_color("#00FF00")
        this.licensepointformat["excellent"] = excellentf
        # good 7-10
        goodf = workbook.add_format({"font_size":11})
        goodf.set_font_name("Dengxian")
        goodf.set_align("center")
        goodf.set_align("vcenter")
        goodf.set_bg_color("#92D050")
        this.licensepointformat["good"] = goodf
        # poor 4-6
        poorf = workbook.add_format({"font_size":11})
        poorf.set_font_name("Dengxian")
        poorf.set_align("center")
        poorf.set_align("vcenter")
        poorf.set_bg_color("#FFFF00")
        this.licensepointformat["poor"] = poorf
        # danger 1-3
        dangerf = workbook.add_format({"font_size":11})
        dangerf.set_font_name("Dengxian")
        dangerf.set_align("center")
        dangerf.set_align("vcenter")
        dangerf.set_bg_color("#FF0000")
        this.licensepointformat["danger"] = dangerf
        # trigger 0
        triggerf = workbook.add_format({"font_size":11})
        triggerf.set_font_name("Dengxian")
        triggerf.set_align("center")
        triggerf.set_align("vcenter")
        triggerf.set_bg_color("#000000")
        triggerf.set_font_color("#FFFFFF")
        this.licensepointformat["trigger"] = triggerf



        # driver group format
        a1f = workbook.add_format({"font_size":11})
        a1f.set_bg_color("#FFFF00")
        a1f.set_font_name("Dengxian")
        a1f.set_align("vcenter")
        this.groupformat["A1"] = a1f
        a2f = workbook.add_format({"font_size":11})
        a2f.set_bg_color("#E26B0A")
        a2f.set_font_name("Dengxian")
        a2f.set_align("vcenter")
        this.groupformat["A2"] = a2f
        a3f = workbook.add_format({"font_size":11})
        a3f.set_bg_color("#00B050")
        a3f.set_font_name("Dengxian")
        a3f.set_align("vcenter")
        this.groupformat["A3"] = a3f



        # LAN username format
        lanf = workbook.add_format({"font_size":11})
        lanf.set_font_name("Dengxian")
        lanf.set_align("vcenter")
        lanf.set_text_wrap()
        this.lanusernameformat["ACTIVE"] = lanf
        this.lanusernameformat["SYSTEM ACCOUNT"] = lanf
        RCf = workbook.add_format({"font_size":11})
        RCf.set_font_name("Dengxian")
        RCf.set_align("vcenter")
        RCf.set_bg_color("#00FF00")
        RCf.set_text_wrap()
        this.lanusernameformat["Race Coordinator"] = RCf
        standbyf = workbook.add_format({"font_size":11})
        standbyf.set_font_name("Dengxian")
        standbyf.set_align("vcenter")
        standbyf.set_bg_color("#FFFF00")
        standbyf.set_text_wrap()
        this.lanusernameformat["STANDBY"] = standbyf

        

        # race result table format
        timef = workbook.add_format({"num_format":"m:ss.000"})
        timef.set_font_size("12")
        timef.set_font_name("Dengxian")
        timef.set_align("center")
        timef.set_align("vcenter")
        this.raceresultformat["timef"] = timef
        headerf = workbook.add_format({"font_size":12})
        headerf.set_font_name("Dengxian")
        headerf.set_align("center")
        headerf.set_align("vcenter")
        this.raceresultformat["headerf"] = headerf
        a1headerf = workbook.add_format({"font_size":12})
        a1headerf.set_font_name("Dengxian")
        a1headerf.set_align("center")
        a1headerf.set_align("vcenter")
        a1headerf.set_bg_color("#FFFF00")
        this.raceresultformat["a1headerf"] = a1headerf
        a2headerf = workbook.add_format({"font_size":12})
        a2headerf.set_font_name("Dengxian")
        a2headerf.set_align("center")
        a2headerf.set_align("vcenter")
        a2headerf.set_bg_color("#E26B0A")
        this.raceresultformat["a2headerf"] = a2headerf
        a3headerf = workbook.add_format({"font_size":12})
        a3headerf.set_font_name("Dengxian")
        a3headerf.set_align("center")
        a3headerf.set_align("vcenter")
        a3headerf.set_bg_color("#00B050")
        this.raceresultformat["a3headerf"] = a3headerf
        laptimef = workbook.add_format({"font_size":12})
        laptimef.set_font_name("Dengxian")
        laptimef.set_align("center")
        laptimef.set_align("vcenter")
        this.raceresultformat["laptime"] = laptimef
        qualibanf = workbook.add_format({"font_size":12})
        qualibanf.set_font_name("Dengxian")
        qualibanf.set_align("center")
        qualibanf.set_align("vcenter")
        qualibanf.set_bg_color("#000000")
        qualibanf.set_font_color("#FFFFFF")
        this.raceresultformat["QB"] = qualibanf
        dnsf = workbook.add_format({"font_size":12})
        dnsf.set_font_name("Dengxian")
        dnsf.set_align("center")
        dnsf.set_align("vcenter")
        dnsf.set_bg_color("#808080")
        this.raceresultformat["DNS"] = dnsf
        retiredf = workbook.add_format({"font_size":12})
        retiredf.set_font_name("Dengxian")
        retiredf.set_align("center")
        retiredf.set_align("vcenter")
        retiredf.set_bg_color("#7030A0")
        this.raceresultformat["RETIRED"] = retiredf
        dnff = workbook.add_format({"font_size":12})
        dnff.set_font_name("Dengxian")
        dnff.set_align("center")
        dnff.set_align("vcenter")
        this.raceresultformat["DNF"] = dnff
        dsqf = workbook.add_format({"font_size":12})
        dsqf.set_font_name("Dengxian")
        dsqf.set_align("center")
        dsqf.set_align("vcenter")
        dsqf.set_bg_color("#FF0000")
        this.raceresultformat["DSQ"] = dsqf
        softtyref = workbook.add_format({"font_size":12})
        softtyref.set_font_name("Dengxian")
        softtyref.set_align("center")
        softtyref.set_align("vcenter")
        softtyref.set_bg_color("#FF0000")
        softtyref.set_bold(True)
        this.raceresultformat["S"] = softtyref
        mediumtyref = workbook.add_format({"font_size":12})
        mediumtyref.set_font_name("Dengxian")
        mediumtyref.set_align("center")
        mediumtyref.set_align("vcenter")
        mediumtyref.set_bg_color("#FFFF00")
        mediumtyref.set_bold(True)
        this.raceresultformat["M"] = mediumtyref
        hardtyref = workbook.add_format({"font_size":12})
        hardtyref.set_font_name("Dengxian")
        hardtyref.set_align("center")
        hardtyref.set_align("vcenter")
        hardtyref.set_bold(True)
        this.raceresultformat["H"] = hardtyref
        intertyref = workbook.add_format({"font_size":12})
        intertyref.set_font_name("Dengxian")
        intertyref.set_align("center")
        intertyref.set_align("vcenter")
        intertyref.set_bg_color("#00B050")
        intertyref.set_bold(True)
        this.raceresultformat["I"] = intertyref
        wettyref = workbook.add_format({"font_size":12})
        wettyref.set_font_name("Dengxian")
        wettyref.set_align("center")
        wettyref.set_align("vcenter")
        wettyref.set_bg_color("#0070C0")
        wettyref.set_bold(True)
        this.raceresultformat["W"] = wettyref
        positionupf = workbook.add_format({"font_size":12})
        positionupf.set_font_name("Dengxian")
        positionupf.set_align("center")
        positionupf.set_align("vcenter")
        positionupf.set_bg_color("#00FF00")
        positionupf.set_text_wrap()
        this.raceresultformat["positionup"] = positionupf
        positiondownf = workbook.add_format({"font_size":12})
        positiondownf.set_font_name("Dengxian")
        positiondownf.set_align("center")
        positiondownf.set_align("vcenter")
        positiondownf.set_bg_color("#FF0000")
        positiondownf.set_text_wrap()
        this.raceresultformat["positiondown"] = positiondownf
        positionholdf = workbook.add_format({"font_size":12})
        positionholdf.set_font_name("Dengxian")
        positionholdf.set_align("center")
        positionholdf.set_align("vcenter")
        positionholdf.set_text_wrap()
        this.raceresultformat["positionhold"] = positionholdf
        fastestlapf = workbook.add_format({"font_size":12})
        fastestlapf.set_font_name("Dengxian")
        fastestlapf.set_align("center")
        fastestlapf.set_align("vcenter")
        fastestlapf.set_bg_color("#7030A0")
        this.raceresultformat["fastestlap"] = fastestlapf
        fakefastestlapf = workbook.add_format({"font_size":12})
        fakefastestlapf.set_font_name("Dengxian")
        fakefastestlapf.set_align("center")
        fakefastestlapf.set_align("vcenter")
        fakefastestlapf.set_bg_color("#000000")
        fakefastestlapf.set_font_color("#FFFFFF")
        this.raceresultformat["fakefastestlap"] = fakefastestlapf
        deniedheaderf = workbook.add_format({"font_size":12})
        deniedheaderf.set_font_name("Dengxian")
        deniedheaderf.set_align("center")
        deniedheaderf.set_align("vcenter")
        deniedheaderf.set_bg_color("#000000")
        deniedheaderf.set_font_color("#FFFFFF")
        this.raceresultformat["deniedheader"] = deniedheaderf


        # race director panel format
        rdheader = workbook.add_format({"font_size":11})
        rdheader.set_font_name("Dengxian")
        rdheader.set_align("vcenter")
        rdheader.set_text_wrap()
        this.racedirector["header"] = rdheader
        rdformat = workbook.add_format({"font_size":11})
        rdformat.set_font_name("Dengxian")
        rdformat.set_align("vcenter")
        rdformat.set_text_wrap()
        this.racedirector["default"] = rdformat
        rdformat2 = workbook.add_format({"num_format": "yyyy/m/dd"})
        rdformat2.set_font_size("11")
        rdformat2.set_font_name("Dengxian")
        rdformat2.set_align("vcenter")
        this.racedirector["date"] = rdformat2