/*
Vaptcha 核心加密JS

Author leng-yue
Date 2018-08-02

Example vcaptcha.assemblyCoordData([{'x': 0, 'y': 0, 'time':0}]);
 */

var vcaptcha = {
    _sample: "abcdefgh234lmntuwxyz",
    _convertScale: function (t) {
        var e, n, i, a, s = this._sample.length, o = Math.abs(t), r = !1, c = "", l = [];
        s <= parseInt(o / s) ? (a = (e = parseInt(t / (s * s))) * s * s,
            l.push(e),
            n = parseInt((t - a) / s),
            l.push(n),
            l.push(t - a - n * s)) : (a = (e = parseInt(t / s)) * s,
            l.push(e),
            l.push(n = t - a),
            r = !0),
        r && (c = "_"),
            i = l.length;
        for (var h = 0; h < i; h++)
            c += this._sample.charAt(l[h]);
        return c
    },
    assemblyCoordData: function (t) {
        for (var e = [], n = [], i = [], a = 0; a < t.length; a++)
            e.push(this._convertScale(t[a].x)),
                n.push(this._convertScale(t[a].y)),
                i.push(this._convertScale(t[a].time));
        return e.join("") + n.join("") + i.join("")
    }
};
