
//This function would be updated to query from the database but this is the basic idea of the function. Query the current list of rules within the database. If there is a rule with the same name, reject the rule.
function addRule(name){
 var rules = ["Rule_One","Rule_Two","Rule_Three"];
    if(rules.includes(name)){
        console.log("Already a rule for this file name");
        return true;
    } else{
        rules.push(name);
        return false;
        }  
}

//There needs to be a test for valid ftp address, more communication would be required for understanding the types of addresses we are recieving. https://ftptest.net/

//This functoin checks to see if the user has entered a valid download link. Currently the CORS policy is blocking me from checking to see if this function is returning valid code


function UrlExists(url)
{
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status!=404;
}


/*There needs to be a test to check to see if the file the user is trying to upload actually exists or not. Currently I am perplexed on how to do this. CORS policy is blocking as well as I believe I will need to make an async call but I am not sure to where.*/

/*There needs to be a function to verify if the user has entered valid FTP credentials. 
--Should this information be verified at rule creation vs when the user hits the sync button
--More research required
*/

function NoDuplicateColumns(colName){
 var cols =["Age","Weight","Height"];
    if(cols.includes(colName)){
        console.log("Already a col named this for this file name");
        return true;
    } else{
        cols.push(colName);
        return false;
        }  
}
