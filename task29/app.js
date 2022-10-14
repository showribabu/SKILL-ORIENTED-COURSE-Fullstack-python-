const express=require('express')//serever
const MongoClient=require('mongodb').MongoClient //mongodb..

//obj..

var app=express()
//path.
var mongo="mongodb://localhost:27017/"

//handler..>to read data from mongo..
app.get('/data',function(req,res){

    //connect to mongo..
    MongoClient.connect(mongo,function(err,db){
        if(err){
            throw err;
        }
        var dbo=db.db('showri');
        dbo.collection('fullstack').find(function(err,results){
            if(err){
                throw err
            }
            var data=[]
            for(let i of results){
                data.push(JSON.stringify(i))
            }
            res.send(data.toString());
        })
    })

})

//server start..

app.listen(2000,function(){
    console.log('Servet start')
})
