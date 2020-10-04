var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");
var math = require("mathjs")


var server = http.createServer(function(req, res){
    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        })
    }
    else if(req.url.match("/sysinfo")){
        myHostName=os.hostname();
        var cpus=os.cpus();
        var live=os.uptime();
        function running(seconds){
        var seconds = Number(seconds);
        var days = Math.floor(seconds/(3600*24));
        seconds = seconds - (days*3600*24);
        var hours = Math.floor(seconds/3600);
        seconds = seconds - (hours*3600);
        var minutes = Math.floor(seconds/60);
        seconds = seconds - (minutes*60);
        return days+" days, "+hours+" hours, "+minutes+" minutes, and "+seconds+" seconds";
        }
        var fmem=os.freemem();
        fmemMB= fmem / 1000000;
        var tmem=os.totalmem();
        tmemMB= tmem / 1000000;
        html=`
        <!DOCTYPE html>
        <html>
        <head>
            <title>System Information</title>
        </head>
        <body>
            <p> Hostname: ${myHostName} </p>
            <p> IP: ${ip.address()} </p>
            <p> Server Uptime: ${running(live)} </p>
            <p> Total Memory: ${tmemMB} MB</p>
            <p> Free Memory: ${fmemMB} MB</p>
            <p> Number of CPUS: ${cpus.length} </p>
        </body>
        </html>
        `
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/html"});
        res.end(`404 File Not Found at ${req.url}`);
    }

    //res.writeHead(200 ,{"Content-Type": "text/html"});
    //res.end();
}
);

server.listen(3000);

console.log("Im listening >:)");
