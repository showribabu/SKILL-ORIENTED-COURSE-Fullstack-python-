//server,mongodb,read from getmethod..>parser..

const express=require('express');
const { request } = require('http');
//mongodb..27017..
const MongoClient=require('mongodb').MongoClient;
//parser..by use..get method..
const url=require('url')

//obj..

var app=express()
var mongo="mongodb://localhost:27017/"


//handlers..

app.get('/book',function(request,res){
    //here data from /book in the reuest attrtibute..
    //now from request data can br parse....
    urldata=url.parse(request.url,true);
    //now data in urldata..
    var name=urldata.query.bookname;
    var cataegory=urldata.query.category;

    //now dta retrived..
    //connect tpo database at mongo ..localhost://27017..

    MongoClient.connect(mongo,function(err,db){
        if(err){
            throw err;
        }
        var dbo=db.db('showri');
        var doc={'name':name,'categ':cataegory};
        dbo.collection('fullstack').insertOne(doc,function(err,result){
            if(err){
                throw err
            }
            res.end('Data inserted Sucessfully');
        })


    })

})


//server..start..
app.listen(2000,function(){
    console.log('Server Start');
})


///starrt in postman...
