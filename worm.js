window.onload=function() {
	canv = document.getElementById("snake");
	ctx = canv.getContext("2d");
	document.addEventListener("keydown",keyPush);
	setInterval(game,1000/10);
}
function reset() {
	// player x and y position
	player_x = 10;
	player_y = 10;
	
	//set grid size to 20 x 20
	grid_size = 20;
	tileCount = 20;
	
	//player x and y speed
	x_speed = 0;
	y_speed = 0;
	d = "null my man"
	
	// apple pos
	apple_x = 15;
	apple_y = 15;
	
	//store the whole snake x and y positions
	trail=[];
	// starting length
	tail = 3;
}
pause = false
reset();
// number of lives
deaths = 0;
highscore = 0;
//game logic goes here
function game(){
	if (pause === false) {
		//update player position each frame
		player_x+=x_speed;
		player_y+=y_speed;
		
		/*
		//detecting boundries
		if(player_x < 0) {
			reset();
			deaths++;
		}//end of "if(player_x < 0)"
		if(player_x > 20) {
			reset();
			deaths++;
		}
		if(player_y < 0) {
			reset();
			deaths++;
		}//end of "if(player_x < 0)"
		if(player_y > 20) {
			reset();
			deaths++;
		}//end of "if(player_x > tileCount - 1)"
		*/
		
		//create black background
		ctx.fillStyle="black";
		ctx.fillRect(0,0,canv.width,canv.height);
		
		//draw the snake
		ctx.fillStyle="green"
		for(var i=0;i<trail.length;i++) {
			ctx.fillStyle = "#e5bc69"
			ctx.fillRect(trail[i].x*grid_size, trail[i].y*grid_size,grid_size-2,grid_size-2);
			if(trail[i].x==player_x && trail[i].y==player_y) {
				// set the snake back to 5
				if (d != "null my man") {
					deaths++;
					reset();
				}
				tail = 3;
	
			}//end of "if(trail[i].x==player_x && trail[i].y==player)"
		}//end of "for(var i=0;i<trail.length;i++)"
		trail.push({x:player_x,y:player_y});
		while(trail.length>tail) {
			//this deletes the first value in an array
			trail.shift();
		}// end of "while(trail.length>tail)"
		
		//detecting boundries
		if(player_x < 0) {
			reset();
			deaths++;
		}//end of "if(player_x < 0)"
		if(player_x > tileCount-1) {
			reset();
			deaths++;
		}
		if(player_y < 0) {
			reset();
			deaths++;
		}//end of "if(player_x < 0)"
		if(player_y > tileCount-1) {
			reset();
			deaths++;
		}//end of "if(player_x > tileCount - 1)"
		
		//store the x and y positions of the snake
		
		//detect apple collision
		if(apple_x == player_x && apple_y == player_y) {
			// adding 1 to the tail length
			tail++;
			// moving to random x and y
			apple_x = Math.floor(Math.random()*tileCount);
			apple_y = Math.floor(Math.random()*tileCount);
		}
		//draw the apple
		ctx.fillStyle="#8e8c87";
		ctx.fillRect(apple_x*grid_size,apple_y*grid_size,grid_size-2,grid_size-2);
		
		// highscore
		if ((tail-3) > highscore){highscore = tail-3;}
		
		// draw lives
		ctx.fillStyle="#ffe41e"
		ctx.font= canv.width/15+"px Comic Sans MS";
		ctx.fillText("number of deaths: "+(deaths), 0, canv.height/13);
		ctx.fillText("rocks eaten: "+(tail-3), 0, canv.height/7);
		//if (highscore !== 0){
		ctx.fillText("highscore: "+(highscore), 0, canv.height/5);
		//}
	} else {
		ctx.fillStyle="blue";
		ctx.font = canv.width/5+"px Comic Sans MS";
		ctx.fillText("█ █",canv.width/3,(canv.height/3)*1.5);
	}
}// end of function "game"

function keyPush(evt) {
	switch(evt.keyCode) {
		case 37: // left arrow
			if (d!="right"){ x_speed = -1; y_speed = 0; d = "left"} 
			break;
		case 38: // up arrow
			if (d!="down"){ x_speed = 0; y_speed = -1; d = "up"} 
			break;
		case 39: // right arrow
			if (d!="left"){ x_speed = 1; y_speed = 0; d = "right"} 
			break;
		case 40: // down arrow
			if (d!="up"){ x_speed = 0; y_speed = 1; d = "down"} 
			break;
		case 80: //"p" key
			pause = pause === false // im proud of this 
	}
}
