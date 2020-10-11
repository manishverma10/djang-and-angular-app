import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  title = 'string pattern checker';
  

  getKeyValuePair(val){
    var newobj = {};
    val.split(' ').forEach(function (value) {
        var keypair = value.split('=');
        newobj[keypair[0]] = keypair[1];
    });
    
    return newobj;
  }

  
  clickFunction() {
    // const str = '((a=1 && b=2) || (c=3 && d=4))';
    const str = document.getElementById("inputText").value;
    const strArr = str.split('||')
    const strFormat = ['(',')'];
    let isValidString = true
  
    strArr.some(word => {
      strFormat.some(parethesis => {
        if(word.includes(parethesis)){
          if (word.includes('&&')) {
            // pass
          } else{
            isValidString = false;
          return false;
          }
        } else{
          isValidString = false;
        return false;
        }
      })
    });
  
  
    if (isValidString) {
  
      let objTrim =  str.replace(/\&\&/g, '').replace(/\(/g, '').replace(/\)/g, '').replace(' ', '');
  
      let objTrimArr = objTrim.split('||');
  
      let andFormat = '';
  
        objTrimArr.forEach(element => {
  
          element = this.getKeyValuePair(element)
  
            andFormat += `
              {
              "and": 
                ${JSON.stringify(element)}
              },`;
  
        });
  
        const completeStr = `
        {
          "query": {
            "or": [
              ${andFormat}
            ]
          }
        }`;
  
        console.log(completeStr)
        document.querySelector("#resultBar").value = completeStr;
        document.querySelector(".label-control").innerText= "Result Bar: Valid Expression";
        document.getElementById("resultDiv").style.display = "block";
  
    } else{
      // console.log("Invalid Expression")
      document.querySelector("#resultBar").value = "Invalid Expression";
      document.getElementById("resultDiv").style.display = "block";
      document.querySelector(".label-control").innerText= "Result Bar: Invalid Expression";
    }
  }

  
}
