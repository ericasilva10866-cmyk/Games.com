<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Jogo da Cobrinha Viciante</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: #111;
            color: #fff;
            font-family: sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            overflow: hidden;
        }
        #placar { font-size: 24px; font-weight: bold; margin-bottom: 10px; color: #4CAF50; }
        canvas { background: #222; border: 4px solid #4CAF50; border-radius: 8px; box-shadow: 0 0 20px rgba(76, 175, 80, 0.3); }
        .controles {
            display: grid;
            grid-template-columns: repeat(3, 70px);
            grid-template-rows: repeat(3, 70px);
            gap: 10px;
            margin-top: 20px;
        }
        .btn {
            background: #333;
            border: 2px solid #4CAF50;
            border-radius: 50%;
            color: white;
            font-size: 24px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            user-select: none;
        }
        .btn:active { background: #4CAF50; }
        #btn-cima { grid-column: 2; grid-row: 1; }
        #btn-esq { grid-column: 1; grid-row: 2; }
        #btn-dir { grid-column: 3; grid-row: 2; }
        #btn-baixo { grid-column: 2; grid-row: 3; }
    </style>
</head>
<body>

    <div id="placar">Pontos: 0</div>
    <canvas id="jogo" width="300" height="300"></canvas>

    <!-- Botões de seta para jogar no celular -->
    <div class="controles">
        <div class="btn" id="btn-cima">↑</div>
        <div class="btn" id="btn-esq">←</div>
        <div class="btn" id="btn-dir">→</div>
        <div class="btn" id="btn-baixo">↓</div>
    </div>

    <script>
        const canvas = document.getElementById("jogo");
        const ctx = canvas.getContext("2d");
        const placarTxt = document.getElementById("placar");

        const tamanhoBloco = 15;
        let cobrinha = [{ x: 150, y: 150 }];
        let maca = { x: 0, y: 0 };
        let dx = tamanhoBloco;
        let dy = 0;
        let pontos = 0;
        let velocidade = 120;
        let jogoLoop;

        function iniciarJogo() {
            criarMaca();
            jogoLoop = setTimeout(mudarDirecao, velocidade);
        }

        function criarMaca() {
            maca.x = Math.floor(Math.random() * (canvas.width / tamanhoBloco)) * tamanhoBloco;
            maca.y = Math.floor(Math.random() * (canvas.height / tamanhoBloco)) * tamanhoBloco;
        }

        function mudarDirecao() {
            if (testarFimJogo()) {
                alert("Você bateu! Pontuação final: " + pontos);
                document.location.reload();
                return;
            }

            clearCanvas();
            desenharMaca();
            moverCobrinha();
            desenharCobrinha();

            jogoLoop = setTimeout(mudarDirecao, velocidade);
        }

        function clearCanvas() {
            ctx.fillStyle = "#222";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }

        function desenharCobrinha() {
            ctx.fillStyle = '#4CAF50';
            cobrinha.forEach(parte => {
                ctx.fillRect(parte.x, parte.y, tamanhoBloco - 2, tamanhoBloco - 2);
            });
        }

        function moverCobrinha() {
            const cabeca = { x: cobrinha[0].x + dx, y: cobrinha[0].y + dy };
            cobrinha.unshift(cabeca);

            if (cobrinha[0].x === maca.x && cobrinha[0].y === maca.y) {
                pontos += 10;
                placarTxt.innerText = "Pontos: " + pontos;
                if (velocidade > 50) velocidade -= 3;
                criarMaca();
            } else {
                cobrinha.pop();
            }
        }

        function desenharMaca() {
            ctx.fillStyle = '#FF5252';
            ctx.fillRect(maca.x, maca.y, tamanhoBloco - 2, tamanhoBloco - 2);
        }

        function testarFimJogo() {
            for (let i = 4; i < cobrinha.length; i++) {
                if (cobrinha[i].x === cobrinha[0].x && cobrinha[i].y === cobrinha[0].y) return true;
            }
            return cobrinha[0].x < 0 || cobrinha[0].x >= canvas.width || cobrinha[0].y < 0 || cobrinha[0].y >= canvas.height;
        }

        // Comandos dos botões na tela do celular
        document.getElementById("btn-cima").addEventListener("touchstart", (e) => { e.preventDefault(); if (dy === 0) { dx = 0; dy = -tamanhoBloco; } });
        document.getElementById("btn-baixo").addEventListener("touchstart", (e) => { e.preventDefault(); if (dy === 0) { dx = 0; dy = tamanhoBloco; } });
        document.getElementById("btn-esq").addEventListener("touchstart", (e) => { e.preventDefault(); if (dx === 0) { dx = -tamanhoBloco; dy = 0; } });
        document.getElementById("btn-dir").addEventListener("touchstart", (e) => { e.preventDefault(); if (dx === 0) { dx = tamanhoBloco; dy = 0; } });

        iniciarJogo();
    </script>
</body>
</html>
