const imagem1 = document.getElementById('chuckie2')
const botao1 = document.getElementById("botao")

// função que muda as imagens do Chuckie
botao1.onclick=function(){
    if(botao1.value === "valor1"){
        alert('Chuckie Assustado!')
        imagem1.src='imgs-chuckie/chuckie-1.jpg';
        botao1.value ="valor2";
        
    }
    else if(botao1.value === "valor2"){
        alert('Chuckie Feliz!')
        imagem1.src='imgs-chuckie/chuckie-2.png';
        botao1.value ="valor1";
    }
    console.log("deu certo")
    console.log(botao1)

}

