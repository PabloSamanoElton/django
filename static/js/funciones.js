document.getElementById("buton").addEventListener("click",respuesta);
 
function respuesta(){

    var xhr = new XMLHttpRequest();
 	var z = null;

    xhr.open("GET","prueba",true);
    xhr.send();
	print(idk);
	document.getElementById("buton").innerHTML = xhr.responseText;
	var z = xhr.responseText;  
    
    xhr.onreadystatechange = function(){        
    	
    }
}


<script type="text/javascript">
	function OK(){
		alert(document.getElementById("Nombre").value);
	}
</script>
