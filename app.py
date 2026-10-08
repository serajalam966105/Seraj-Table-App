<!DOCTYPE html>
<html>
<head>
<title>Infinite Table with Photo</title>
<style>
body { font-family: sans-serif; text-align: center; background: #f0f2f5; }
.box { background: white; padding: 20px; max-width: 400px; margin: 30px auto; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
input { padding: 12px; width: 80%; font-size: 18px; border-radius: 8px; border: 1px solid #ccc; text-align: center; margin-top:10px; }
button { padding: 12px 25px; margin-top: 10px; font-size: 18px; background: #007bff; color: white; border: none; border-radius: 8px; cursor: pointer; }
#myPhoto { width: 150px; height: 150px; border-radius: 50%; object-fit: cover; display:none; border: 4px solid #007bff; margin: 0 auto; }
#result { margin-top: 20px; font-size: 20px; line-height: 35px; max-height: 70vh; overflow-y: auto; }
</style>
</head>
<body>

<div class="box">
<img id="myPhoto" src="">
<h2>Table Generator ♾️</h2>

<!-- YAHAN SE PHOTO SELECT HOGA -->
<p><b>Apna JPG Photo Select Karo:</b></p>
<input type="file" id="photoInput" accept="image/jpeg,image/jpg,image/png" onchange="loadPhoto(event)">
<br><br>

<input type="number" id="num" placeholder="Number likho jaise 19">
<br>
<button onclick="generate()">Table Dikhao</button>
<button onclick="more()" style="background:green;">Aur +100 Tak</button>
<div id="result"></div>
</div>

<script>
let currentNum = 0;
let currentLimit = 0;

function loadPhoto(event) {
    let photo = document.getElementById("myPhoto");
    photo.src = URL.createObjectURL(event.target.files[0]);
    photo.style.display = "block";
}

function generate() {
    let n = document.getElementById("num").value;
    if(n=="") { alert("Pehle number likho!"); return; }
    currentNum = n;
    currentLimit = 100;
    showTable();
}

function more() {
    if(currentNum==0) { alert("Pehle koi table banao!"); return; }
    currentLimit += 100;
    showTable();
}

function showTable() {
    let res = "";
    for(let i=1; i<=currentLimit; i++) {
        res += `${currentNum} x ${i} = ${currentNum*i} <br>`;
    }
    document.getElementById("result").innerHTML = res + `<br><b>${currentLimit} tak ho gaya</b>`;
}
</script>

</body>
</html>
