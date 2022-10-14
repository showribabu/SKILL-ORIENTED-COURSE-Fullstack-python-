const express=require('express')//serever
const url=require('url')//data
const MongoClient=require('mongodb').MongoClient  //data store

//obj..

var app=express()
var mongo="mongodb://localhost:27017/"

//handlers
app.get('/data',function(request,response){

    var urldata=url.parse(request.url,true)
    var name=urldata.query.bookname
    MongoClient.connect(mongo,function(err,db){
        if(err)
        {
            throw err
        }
        var dbo=db.db('showri');
        var doc={'name':name}
        dbo.collection('fullstack').insertOne(doc,function(err,result){
            if(err){
                throw err;
            }
         console.log('data inserted');

        })
        dbo.collection('fullstack').find(function(err,results){
            if(err)
            {
                throw err;
            }
            var data=[]
            for(let i of results){
                    data.push(JSON.stringify(i))
                    }
                response.send(data.toString())
        })

    })
})

//server start..
app.listen(2000,function(){
    console.log('server start')
})