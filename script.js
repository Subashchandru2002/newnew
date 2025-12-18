function greetUser() {
    // SOURCE: Untrusted data from the URL hash
    var name = window.location.hash.substring(1);
    
    // SINK: Using innerHTML allows script execution
    // This should trigger: "Cross-site scripting"
    document.getElementById('greeting').innerHTML = "Hello, " + name;
}
