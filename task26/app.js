//for server express..,files.. dataretrive(parse)....database sql..

const express=require('express')
const fs=require('fs')

//sql...
const mysql=require('mysql2')

const parser=require('body-parser')

//obj..

var app=express()
var encodedp=parser.urlencoded({'extented':false});

//...connection to the mysql..

var conn=mysql.createConnection({
host:'localhost',user:'root',password:'kits',database:'showri'
})

//handlers..

//1)file show..

app.get('/',function(req,res){
    fs.readFile('form.html',function(err,data){
if(err)
{
    throw err
}
res.end(data)//send..
    })
})

//2)read..parsing by use post method..

app.post('/add',encodedp,function(req,res)
{
    var name=req.body.name;
    var author=req.body.author;
    var category=req.body.category;
    var branch=req.body.branch;
    var year=req.body.year;
    //connection to database..
    conn.connect(function(err){
        if(err){
            throw err
        }
    })
    var sql="insert into book values('"+name+"','"+author+"','"+category+"','"+branch+"','"+year+"')"
    conn.query(sql,function(err,response){
        if(err){
            throw err
        }
        res.send('data Inserted Sucessfully')
    })


})

//servere

app.listen(2000,function(){
    console.log('Server Start')
})