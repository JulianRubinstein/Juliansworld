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
    var elem = document.getElementById('cell-' + cellNum)
    elem.setAttribute("value", cellValue)
}

//Function that deletes the value of a cell
function delNum(cellNum){
    var elem = document.getElementById('cell-' + cellNum)
    elem.removeAttribute("value")
}

//Aesthetic function
function mapValue(cellNum){
    return document.getElementById('cell-' + cellNum).value
    }

//Aesthetic function
function mapClass(cellNum){
    return document.getElementById('cell-' + cellNum).className
}

//A function that checks if a certain cell has a valid number according to sudoku rules
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

//The same as check valid except for allowing empty strings for initial checking
function checkIfValidInitial(i,j){
    //Checks if column contains same number
    if(!(mapValue(grid[i][j])=="")){
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
    }
    return true
}

//A function that checks all posibilities for a certain cell using the check if valid function
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

//Similar to above function but instead of checking from zero, checks from the previously held number
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

//Function that cleans the board
function clean(){
    location.reload()
}

function listener(){
  let cells = document.getElementsByClassName("cell")
  for (let i=0; i<81; i++){
    cells[i].addEventListener('change', function() {
      cells[i].setAttribute("readonly", true)
      })
    }
}

//Function that is called when user presses "solve"
//The main function - This calls producenum and producenumback to solve each cell
//When finished, makes all the cells readonly
function solve(){
  if (checkValidInput()){
    alert("Invalid input :(")
    location.reload()
    return
  }
    var i=0, j=0
    while(i!=9){
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

    let cells = document.getElementsByClassName("cell")
    for (let i=0; i<81; i++){
        cells[i].setAttribute("readonly", true)
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

//Initial check that the board has valid input
function checkValidInput(){
  let checker
  let cells = document.getElementsByClassName("cell")
  let nums = ["1","2","3","4","5","6","7","8","9",""]
  for (let i=0; i<81; i++){
      if (!(nums.includes(cells[i].value))){
            return true
      }
    }

  for (let i=0; i<9; i++){
    for (let j=0; j<9; j++){
      checker = checkIfValid(i,j)
      if (checkIfValidInitial(i,j)==false){
        return true
      }
    }
  }
  return false
}

listener()
