function format(n) {
    var nstr = [];
    while (n > 1000) {
        var d = "000" + (n % 1000);
        d = d.substr(d.length - 3, 3);
        nstr.unshift(d);
        n = n / 1000 | 0;
    }
    if (n != 0)
        nstr.unshift(n);
    return nstr.join(",");
}

function percentage(x, y) {
    var pc = (Math.round(1000 * x / y) / 10) + "";
    if (pc.indexOf(".") < 0)
        pc += ".0";
    return pc + "%";
}

function drawChart(name) {

    $.getJSON("data/" + name + ".json", function(data) {

        var colourTotals = {}, grouped = false;
        $.each(data, function(key, party) {
            var colour = party["color"];
            if (colour in colourTotals) {
                colourTotals[colour] += party["user"]["followers_count"];
                grouped = true;
            } else {
                colourTotals[colour] = party["user"]["followers_count"];
            }
        });

        // add up total followers
        var totalFollowers = 0;
        $.each(data, function(key, party) {
            totalFollowers += party["user"]["followers_count"];
        });

        if (grouped) {
            var data2 = {};
            $.each(data, function(key, party) {
                var colour = party["color"];
                if (!(colour in data2)) {
                    data2[colour] = {
                        "name": party["name"],
                        "screen_names": [],
                        "color": colour,
                        "user": {
                            "followers_count": 0
                        }
                    };
                }
                data2[colour]["screen_names"].push("@" + key);
                data2[colour]["user"]["followers_count"] += party["user"]["followers_count"];
            });
            $.each(data2, function(colour, blob) {
                data2[colour]["name"] += " (" + data2[colour]["screen_names"].join(" + ") + ")";
            });
            data = data2;
        }

        // extract values
        var parties = [], values = [], legend = [], colors = [], urls = [];
        $.each(data, function(key, party) {
            var followers = party["user"]["followers_count"];
            if (grouped) {
                legend.push(this["name"] + " - " + format(followers) + " (" + percentage(followers, totalFollowers) + ")");
            } else {
                legend.push(this["name"] + " (@" + key + ") - " + format(followers) + " (" + percentage(followers, totalFollowers) + ")");
            }
            values.push(followers);
            party["screen_name"] = key;
            if (parties.length == 0) {
                parties.push(party);
            } else {
                var inserted = false;
                for (var i = 0; i < parties.length; ++i) {
                    if (followers > parties[i]["user"]["followers_count"]) {
                        parties.splice(i, 0, party);
                        inserted = true;
                        break;
                    }
                }
                if (!inserted) {
                    parties.push(party);
                }
            }
        });
        
        $.each(parties, function() {
            colors.push(this["color"]);
            if (!grouped) {
                urls.push("https://twitter.com/" + this["screen_name"]);
            }
        });
        
        var r = Raphael(name, 960, 320);
        r.piechart(200, 160, 150, values, {
            "colors": colors,
            "href": urls,
            "init": false,
            "legend": legend,
            "minPercent": 0.499
        });
        
    });

}

