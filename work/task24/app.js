const express=require('express');

const fs=require('fs');
//use to render files to server..


//obj
var app=express();

//handlers for 2 html files..

app.get('/home',function(req,res){
    fs.readFile('HOME.HTML',function(err,data){
        if(err){
            throw(err);
        }
        res.end(data);
    })
})

app.get('/about',function(req,res){
    fs.readFile('about.html',function(err,data){
        if(err){
            throw(err);
        }
        res.end(data);
    })
})

//server..

app.listen(2000,function(){
    console.log('server strated');
})