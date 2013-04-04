$(document).ready(function() {

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
        
        var r = Raphael("parties", 960, 440);
        r.piechart(300, 220, 200, values, {
            "colors": colors,
            "href": urls,
            "init": false,
            "legend": legend,
            "minPercent": 0.01
        });
        
    });

    $.getJSON("leaders.json", function(data) {

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
        
        var r = Raphael("leaders", 960, 440);
        r.piechart(300, 220, 200, values, {
            "colors": colors,
            "href": urls,
            "init": false,
            "legend": legend,
            "minPercent": 0.01
        });

    });
        
    $.getJSON("youth.json", function(data) {

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
        
        var r = Raphael("youth", 960, 440);
        r.piechart(300, 220, 200, values, {
            "colors": colors,
            "href": urls,
            "init": false,
            "legend": legend,
            "minPercent": 0.01
        });
        
    });

});
