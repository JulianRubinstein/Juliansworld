    //Function that creates a grid which maps the i,j cordinate to cell number
    function makeGrid(){
              var grid = [[ 0, 1, 2, 3, 4, 5, 6, 7, 8],
                          [9, 10,11,12,13,14,15,16,17],
                          [18,19,20,21,22,23,24,25,26],
                          [27,28,29,30,31,32,33,34,35],
                          [36,37,38,39,40,41,42,43,44],
                          [45,46,47,48,49,50,51,52,53],
                          [54,55,56,57,58,59,60,61,62],
                          [63,64,65,66,67,68,69,70,71],
                          [72,73,74,75,76,77,78,79,80]] 
              return grid
    }

    //Global paramaters "p" that dicatates wether the algorithm moves "forwards" or "backwards" and the grid variable
    var p=1
    var grid = makeGrid()
        
    //This is a function that replaces a cell number with a cell value
    function replaceNum(cellNum, cellValue){
        var elem = document.getElementById('cell-' + cellNum);
        elem.setAttribute("value", cellValue)    
    }
    
    //Function that deletes the value of a cell
    function delNum(cellNum){
        var elem = document.getElementById('cell-' + cellNum)
        elem.removeAttribute("value")
    }
    
    //    
    function mapValue(cellNum){
        return document.getElementById('cell-' + cellNum).value
        }
      
    //    
    function mapClass(cellNum){
        return document.getElementById('cell-' + cellNum).className
    }
       
    //    
    function checkIfValid(i,j){
        //Checks if column contains same number
        for (let k=0; k<9; k++){
            if (k!==i){
                if (mapValue(grid[i][j]) == mapValue(grid[k][j])){
                    return false
                }
            }
        }
    
        
        //Checks if row contains same number
        for (let k=0; k<9; k++){
            if (k!==j){
                if (mapValue(grid[i][j]) == mapValue(grid[i][k])){
                    return false
                }
            }
        }
        
        //Check if block contains same number
        for (let k=i-i%3; k<i+(3-i%3); k++){
            for (l=j-j%3; l<j+(3-j%3); l++){
                if (k!==i || l!==j){
                    if (mapValue(grid[i][j]) == mapValue(grid[k][l])){
                        return false
                    }
                }
            }
        }
        
        return true
    }
       
    //    
    function produceNum(i,j){
        for (n=1; n<10; n++){
            replaceNum(grid[i][j],n)
            if (checkIfValid(i,j) == true){
                p=1
                return true
            }
        }
        delNum(grid[i][j])
        p=0
        return false
    }
    
    //    
    function produceNumBack(i,j){
        var prev = mapValue(grid[i][j])
        for (var n=(1+parseInt(prev)); n<10; n++){
            replaceNum(grid[i][j],n)
            if (checkIfValid(i,j) == true){
                p=1
                return true
            }
        }
        delNum(grid[i][j])
        p=0
        return false
    }
    
    //
    function clean(){
        for (k=0; k<81; k++){
            delNum(k)
            document.getElementById('cell-' + k).className="cell"
            }
        }
        
    //    
    function solve(){
        var i=0, j=0
        while(i!=9){  
            console.log("hi")
            if (mapClass(grid[i][j])=="cell" & p==1){
                produceNum(i,j)
            }
            if (mapClass(grid[i][j])=="cell" & p==0){
                produceNumBack(i,j)  
            }
            if (p==1){
                if (j==8){
                    i+=1
                    j=0
                    }
                else{
                    j+=1  
                }
            }
            if (p==0){        
                if (j==0){
                    i-=1
                    j=8
                }
                else{
                    j-=1
                }
            }
        }
    }
    
    //Makes default values of cells immutable
    function defaultCells(){
        for (let k=0; k<81; k++){
            if ((document.getElementById('cell-' + k).value)!=0){
                document.getElementById('cell-' + k).className = "cell immutable"
            }
        }
    }

    //
    function go(){
        //defaultCells()
        solve()
    }

    //
    function init(){
        clean()
    }
    
    //
    function httpGetAsync(theUrl, callback) {
	    var xmlHttp = new XMLHttpRequest();
	    xmlHttp.onreadystatechange = function() {
	        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
	            callback(xmlHttp.responseText);
	    }
	    xmlHttp.open("GET", theUrl, true); // true for asynchronous
	    xmlHttp.send(null);
	}
    
    //
    function fillButton(){
        httpGetAsync("http://127.0.0.1:5003/", function(response){
                     alert(response)
                     })
        }

    //
//    function fill(){
//        var board = httpGetAsync("http://127.0.0.1:5003/", function(response){
//                     alert(response)
//                     })
//        }
//    }
    
    //Make Button for sudoku
    //Add comments
    //document.getElementById('cell-' + k).disabled = false (and beautify)
    //Take care of ajax problem?