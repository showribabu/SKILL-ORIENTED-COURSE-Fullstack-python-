const express=require('express')
const fs=require('fs')
// parsing needed..
const parser=require('body-parser')

//obj..

 var app=express()

 //.....
 var encodedp=parser.urlencoded({'extended':false})

//handler..

//1)for open file form..
app.get('/',function(req,res){
    fs.readFile('form.html',function(err,data){
        if (err)
        {
            throw err
        }
        res.end(data)

    })
})

//2)handler for read data by parsing...>parser-body..>urlencoded({'extended':false})

app.post('/add',encodedp,function(req,res){
    console.log(req.body.name);
    console.log(req.body.author);
    console.log(req.body.category);
    console.log(req.body.branch);
    console.log(req.body.year);
    res.send('data collected')

})


//server..

app.listen(2000,function(){
console.log('server started');
})
