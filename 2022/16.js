let valves = ['QR', 'UE', 'MB', 'ZE', 'TL', 'VK', 'WV', 'IV', 'OF', 'QB', 'XK', 'AQ', 'LG', 'SB', 'DC']
let weights = {AWAA: 3, AAAW: 3, LGTL: 2, TLLG: 2, LGXK: 7, XKLG: 7, LGSB: 10, SBLG: 10, LGOF: 4, OFLG: 4, LGQB: 6, QBLG: 6, LGIV: 6, IVLG: 6, LGQR: 8, QRLG: 8, LGZE: 2, ZELG: 2, LGMB: 3, MBLG: 3, LGVK: 13, VKLG: 13, LGUE: 5, UELG: 5, LGAA: 2, AALG: 2, LGAQ: 5, AQLG: 5, LGDC: 7, DCLG: 7, LGWV: 3, WVLG: 3, TLXK: 9, XKTL: 9, TLSB: 12, SBTL: 12, TLOF: 6, OFTL: 6, TLQB: 8, QBTL: 8, TLIV: 8, IVTL: 8, TLQR: 10, QRTL: 10, TLZE: 3, ZETL: 3, TLMB: 3, MBTL: 3, TLVK: 15, VKTL: 15, TLUE: 7, UETL: 7, TLAA: 4, AATL: 4, TLAQ: 5, AQTL: 5, TLDC: 9, DCTL: 9, TLWV: 5, WVTL: 5, OMAA: 4, AAOM: 4, XKSB: 5, SBXK: 5, XKOF: 3, OFXK: 3, XKQB: 3, QBXK: 3, XKIV: 5, IVXK: 5, XKQR: 7, QRXK: 7, XKZE: 7, ZEXK: 7, XKMB: 7, MBXK: 7, XKVK: 8, VKXK: 8, XKUE: 4, UEXK: 4, XKAA: 5, AAXK: 5, XKAQ: 9, AQXK: 9, XKDC: 2, DCXK: 2, XKWV: 6, WVXK: 6, IMAA: 3, AAIM: 3, BGAA: 9, AABG: 9, MPAA: 10, AAMP: 10, SBOF: 8, OFSB: 8, SBQB: 8, QBSB: 8, SBIV: 8, IVSB: 8, SBQR: 10, QRSB: 10, SBZE: 10, ZESB: 10, SBMB: 10, MBSB: 10, SBVK: 3, VKSB: 3, SBUE: 5, UESB: 5, SBAA: 8, AASB: 8, SBAQ: 12, AQSB: 12, SBDC: 3, DCSB: 3, SBWV: 11, WVSB: 11, XBAA: 4, AAXB: 4, MAAA: 3, AAMA: 3, CDAA: 3, AACD: 3, VLAA: 4, AAVL: 4, OFQB: 5, QBOF: 5, OFIV: 2, IVOF: 2, OFQR: 4, QROF: 4, OFZE: 4, ZEOF: 4, OFMB: 4, MBOF: 4, OFVK: 11, VKOF: 11, OFUE: 3, UEOF: 3, OFAA: 2, AAOF: 2, OFAQ: 6, AQOF: 6, OFDC: 5, DCOF: 5, OFWV: 3, WVOF: 3, VFAA: 6, AAVF: 6, CSAA: 7, AACS: 7, HKAA: 7, AAHK: 7, RLAA: 6, AARL: 6, QBIV: 3, IVQB: 3, QBQR: 5, QRQB: 5, QBZE: 8, ZEQB: 8, QBMB: 8, MBQB: 8, QBVK: 11, VKQB: 11, QBUE: 3, UEQB: 3, QBAA: 6, AAQB: 6, QBAQ: 10, AQQB: 10, QBDC: 5, DCQB: 5, QBWV: 3, WVQB: 3, QNAA: 5, AAQN: 5, IVQR: 2, QRIV: 2, IVZE: 6, ZEIV: 6, IVMB: 6, MBIV: 6, IVVK: 11, VKIV: 11, IVUE: 3, UEIV: 3, IVAA: 4, AAIV: 4, IVAQ: 8, AQIV: 8, IVDC: 5, DCIV: 5, IVWV: 5, WVIV: 5, QRZE: 8, ZEQR: 8, QRMB: 8, MBQR: 8, QRVK: 13, VKQR: 13, QRUE: 5, UEQR: 5, QRAA: 6, AAQR: 6, QRAQ: 10, AQQR: 10, QRDC: 7, DCQR: 7, QRWV: 7, WVQR: 7, TQAA: 1, AATQ: 1, IRAA: 3, AAIR: 3, JEAA: 3, AAJE: 3, XEAA: 6, AAXE: 6, VOAA: 5, AAVO: 5, ZEMB: 3, MBZE: 3, ZEVK: 13, VKZE: 13, ZEUE: 5, UEZE: 5, ZEAA: 2, AAZE: 2, ZEAQ: 5, AQZE: 5, ZEDC: 7, DCZE: 7, ZEWV: 5, WVZE: 5, JBAA: 3, AAJB: 3, NCAA: 1, AANC: 1, SEAA: 3, AASE: 3, OIAA: 3, AAOI: 3, OWAA: 3, AAOW: 3, MBVK: 13, VKMB: 13, MBUE: 5, UEMB: 5, MBAA: 2, AAMB: 2, MBAQ: 2, AQMB: 2, MBDC: 7, DCMB: 7, MBWV: 6, WVMB: 6, VKUE: 8, UEVK: 8, VKAA: 11, AAVK: 11, VKAQ: 15, AQVK: 15, VKDC: 6, DCVK: 6, VKWV: 14, WVVK: 14, UEAA: 3, AAUE: 3, UEAQ: 7, AQUE: 7, UEDC: 2, DCUE: 2, UEWV: 6, WVUE: 6, ZMAA: 2, AAZM: 2, RZAA: 4, AARZ: 4, WIAA: 4, AAWI: 4, HOAA: 4, AAHO: 4, FOAA: 4, AAFO: 4, AAZZ: 4, ZZAA: 4, AAAQ: 4, AQAA: 4, AACX: 3, CXAA: 3, AAJQ: 5, JQAA: 5, AADC: 5, DCAA: 5, AAZD: 6, ZDAA: 6, AAMJ: 6, MJAA: 6, AAYJ: 1, YJAA: 1, AAVR: 4, VRAA: 4, AAWV: 5, WVAA: 5, AAPS: 3, PSAA: 3, AABH: 1, BHAA: 1, AAZR: 3, ZRAA: 3, AAAI: 3, AIAA: 3, AAXQ: 5, XQAA: 5, AAVY: 1, VYAA: 1, AAKR: 7, KRAA: 7, AQDC: 9, DCAQ: 9, AQWV: 8, WVAQ: 8, DCWV: 8, WVDC: 8}
let frs = {AW: 0, OM: 0, BG: 0, XB: 0, CD: 0, VF: 0, HK: 0, QN: 0, OF: 4, QB: 14, ZE: 7, OW: 0, MA: 0, MP: 0, UE: 9, QR: 24, TQ: 0, SE: 0, AQ: 20, XE: 0, DC: 8, ZM: 0, VK: 21, VR: 0, BH: 0, ZR: 0, JE: 0, IR: 0, FO: 0, AA: 0, ZZ: 0, XQ: 0, WI: 0, VY: 0, XK: 15, CX: 0, JQ: 0, LG: 3, JB: 0, OI: 0, YJ: 0, NC: 0, KR: 0, MB: 17, AI: 0, TL: 16, RL: 0, CS: 0, WV: 25, ZD: 0, IV: 23, PS: 0, RZ: 0, VO: 0, MJ: 0, IM: 0, VL: 0, SB: 18, HO: 0};
valves = new Set(valves);
print = console.log
// print(valves)
let zip = (...rows) => [...rows[0]].map((_,c) => rows.map(row => row[c]));
let sd = (s1, s2) => new Set([...s1].filter((x) => !s2.has(x)));
let sa = (s1, s2) => new Set([...s1, ...s2]);
let max = Math.max;
function val(nodes, open, times) {
    if (open.size == valves.length) {
        return 0
    }
    let rs1 = [], rs2 = [];
    for (let [node, rs, time] of zip(nodes, [rs1, rs2], times)) {
        if (time <= 2)
            continue;
        for (let child of sd(valves, open)) {
            let newt = time - weights[node + child] - 1;
            rs.push([newt * frs[child], child, new Set([child, ...open]), newt]);
        }
    }
    // print(rs1, rs2, sd(nodes, open));
    if (rs1 && rs2) {
        let M = 0;
        let i = 0;
        for (let [p1, child1, open1, time1] of rs1) {
            for (let [p2, child2, open2, time2] of rs2) {
                if (times[0] == 26)
                    print(i++);
                if (child1 == child2)
                    continue;
                M = max(M, p1 + p2 + val([child1, child2], sa(open1, open2), [time1, time2]));
            }
        }
        return M;
    } else if (rs1) {
        let calls = rs1.map(([p1, child1, open1, time1]) => p1 + val([child1, "LOL"], open1, [time1, 0]));
        return max(...[calls])
    } else if (rs2) {
        let calls = rs2.map(([p1, child1, open1, time1]) => p1 + val(["LOL", child1], open1, [0, time1]));
        return max(...[calls])
    } else {
        return 0;
    }
}

print(val(["AA", "AA"], new Set(), [26, 26]))