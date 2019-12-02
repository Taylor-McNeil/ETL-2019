
QUnit.test("DuplicationOfRules",function(assert){
   var TestOne = "Rule_One";
   var TestTwo = "Rule_Two";
   var TestFour = "Rule_Four";
    
    assert.equal(addRule(TestOne),true,"Rule Already Included");
    assert.equal(addRule(TestTwo),true,"Rule Already Included");
    assert.equal(addRule(TestFour),false,"Rule not found");
});

QUnit.test("ValidDownloadLink",function(assert){
   var google = "https://www.google.com";
   var amazon = "https://www.amazon.com";
   var fake = "https://www.DfkJgNdfKjg.comr";
    
    assert.equal(UrlExists(google,404),true);
    assert.equal(UrlExists(amazon,404),true);
    assert.equal(UrlExists(fake,501),false);
});


QUnit.test("NoDuplicateColumns",function(assert){
   var TestOne = "Age";
   var TestTwo = "Gender";
   var TestFour = "Weight";
    
    assert.equal(NoDuplicateColumns(TestOne),true,"Col Name Already Included");
    assert.equal(NoDuplicateColumns(TestTwo),false,"Col Name not found");
    assert.equal(NoDuplicateColumns(TestFour),true,"Col Name Already Included");
});