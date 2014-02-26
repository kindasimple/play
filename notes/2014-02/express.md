Express!
Envy Labs on Feb 21

Connect is  a middleware module for http

app.set makes things globally available to your views

app.use is your middleware that is run on every request

app.get are a few sample routes that match via RE

Middleware

- construct from connect
- takes 2-3 arguments
- roughly controllers

function <getuser> (req, res, next){
next(); //hand off execution to next middleware
}

Getting parameters

- req.param(‘name’) order of search: params, body, query
- req.files object (.path, .type, ) #can be handled by formidable
- bodyParser helps with processing file upload
- req.cookies
- req.xhr

Response

- res.locals
- res.set to set response headers
- res.cookie, res.clearCookie, res.redirect (302 is default)
- res.send(), res.json, res.sendfile
- res.locals is passed into your view. YAY

request module to make requests

truthey/falsey
