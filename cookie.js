document.cookie; // -> "expires=Tue, 14 Oct 2014 20:23:32 GMT; path=/"
document.cookie = 'TEST=1';
document.cookie; // -> "TEST=1; expires=Tue, 14 Oct 2014 20:23:32 GMT; path=/"

console.log(document.cookie)