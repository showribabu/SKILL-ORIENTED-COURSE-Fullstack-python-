//import modules by use...require('require one..')
const express=require('express');

//obj..

var app=express()
//here request handlers like...python...

//there handler start with @app.route('/)

//here.. handler name,,callback function...(req,response...)

app.get('/',function(request,response){
    response.send('showri');
})


//server start...

//here our default server..

app.listen(2000,function(){
    //for to know server start or not
    console.log('server Started..ready to access');
})

