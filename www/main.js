$(document).ready(function() {

    function format(n) {
        var nstr = [];
        while (n > 1000) {
            nstr.unshift(n % 1000);
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

    $.getJSON("parties.json", function(data) {

        var totalFollowers = 0;

        $.each(data, function(key, party) {
            totalFollowers += party["user"]["followers_count"];
        });
    
        var parties = [], values = [], legend = [], colors = [], urls = [];
        
        $.each(data, function(key, party) {
            var followers = party["user"]["followers_count"];
            legend.push(this["name"] + " - " + format(followers) + " (" + percentage(followers, totalFollowers) + ")");
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
            urls.push(this["user"]["url"]);
        });
        
        var r = Raphael("chart", 960, 600);
        r.piechart(300, 240, 200, values, {
            "colors": colors,
            "href": urls,
            "init": false,
            "legend": legend,
            "minPercent": 0.01
        });
        
    });

});