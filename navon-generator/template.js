Qualtrics.SurveyEngine.addOnload(function()
{

});

Qualtrics.SurveyEngine.addOnReady(function()
{
	// When showInstr is true, instructions will show up
	var showInstr = ###instr###;
	// Time to pause before beginning of block. Only works with showInstr == false
	var pause = ###pause###;

	// OrderI sets local/global
	// 0 is local
	// 1 is global
	var orderI = ###orderi###;
	
	// OrderN sets the kind from the pool
	// Orders for local and global from 0, 1, 2, 3 respectively are:
	//var localPool1 = [letterLwithT, letterFwithT, letterFwithH, letterLwithH];
	//var globalPool1 = [letterTwithL, letterTwithF, letterHwithF, letterHwithL];
	//var localPool2 = [letterZwithE, letterYwithE, letterZwithM, letterYwithM];
	//var globalPool2 = [letterEwithY, letterEwithZ, letterMwithY, letterMwithZ];
	
	var orderN = ###ordern###;

	// Set the block number to record in the correct embedded data fields
	var blockNum = ###block_number###;

	// Limits for local and global respectively
	var limitL = ###limitl###;
	var limitG = ###limitg###;

	var leftKey = 49; // 1 key
	var rightKey = 48; // 0 key
	var nextKey = 78; // N key
	
	var chosenImage;

	var rightLetter1 = "H";
	var leftLetter1 = "T";

	var rightLetter2 = "E";
	var leftLetter2 = "M";

	var letterFwithH = "<pre>HHHHH<br>H<br>HHHHH<br>H<br>H</pre>";
	var letterLwithH = "<pre>H<br>H<br>H<br>H<br>HHHHH</pre>";
	var letterFwithT = "<pre>TTTTT<br>T<br>TTTTT<br>T<br>T</pre>";
	var letterLwithT = "<pre>T<br>T<br>T<br>T<br>TTTTT</pre>";

	var letterHwithF = "<pre>F   F<br>F   F<br>FFFFF<br>F   F<br>F   F</pre>";
	var letterHwithL = "<pre>L   L<br>L   L<br>LLLLL<br>L   L<br>L   L</pre>";
	var letterTwithF = "<pre>FFFFF<br>  F  <br>  F  <br>  F  <br>  F  </pre>";
	var letterTwithL = "<pre>LLLLL<br>  L  <br>  L  <br>  L  <br>  L  </pre>";

	var letterZwithE = "<pre>EEEEE<br>   E<br>  E<br> E<br>EEEEE</pre>";
	var letterZwithM = "<pre>MMMMM<br>   M<br>  M<br> M<br>MMMMM</pre>";
	var letterYwithE = "<pre>E   E<br> E E<br>  E<br>  E<br>  E</pre>";
	var letterYwithM = "<pre>M   M<br> M M<br>  M<br>  M<br>  M</pre>";

	var letterEwithY = "<pre>YYYYY<br>Y<br>YYYY<br>Y<br>YYYYY</pre>";
	var letterEwithZ = "<pre>ZZZZZ<br>Z<br>ZZZZ<br>Z<br>ZZZZZ</pre>";
	var letterMwithY = "<pre>Y   Y<br>YY YY<br>Y Y Y<br>Y   Y<br>Y   Y</pre>";
	var letterMwithZ = "<pre>Z   Z<br>ZZ ZZ<br>Z Z Z<br>Z   Z<br>Z   Z</pre>";

	var instr1 = "<p>During each trial a fixation cross (+) will appear in the center of the screen. The next picture will contain either a <strong>T</strong> or <strong>H</strong>. <em>As quickly as possible</em>, indicate whether the picture contains a <strong>T</strong> or <strong>H</strong>.</p><br><p>If an <strong>H</strong> appears, hit the <strong>number 0 key</strong> situated above the letter P on your keyboard.</p><p>If a <strong>T</strong> appears, hit the <strong>number 1 key</strong> situated above the letter Q on your keyboard.</p><br><p><em>This is a timed task. It is important that you respond as <strong>quickly</strong> and <strong>accurately</strong> as possible.</em></p><br><p>When you are ready to begin, <strong>please hit the N key</strong>.</p>";
	var instr2 = "<p>During each trial a fixation cross (+) will appear in the center of the screen. The next picture will contain either an <strong>E</strong> or <strong>M</strong>. <em>As quickly as possible</em>, indicate whether the picture contains an <strong>E</strong> or <strong>M</strong>.</p><br><p>If an <strong>E</strong> appears, hit the <strong>number 0 key</strong> situated above the letter P on your keyboard.</p><p>If an <strong>M</strong> appears, hit the <strong>number 1 key</strong> situated above the letter Q on your keyboard.</p><br><p><em>This is a timed task. It is important that you respond as <strong>quickly</strong> and <strong>accurately</strong> as possible.</em></p><br><p>When you are ready to begin, <strong>please hit the N key</strong>.</p>";
	 
	var localPool1 = [letterLwithT, letterFwithT, letterFwithH, letterLwithH];
	var localPoolName1 = ["letterLwithT", "letterFwithT", "letterFwithH", "letterLwithH"];
	var correctLocal1 = ["T","T","H","H"];

	var globalPool1 = [letterTwithL, letterTwithF, letterHwithF, letterHwithL];
	var globalPoolName1 = ["letterTwithL", "letterTwithF", "letterHwithF", "letterHwithL"];
	var correctGlobal1 = ["T","T","H","H"];

	var localPool2 = [letterZwithE, letterYwithE, letterZwithM, letterYwithM];
	var localPoolName2 = ["letterZwithE", "letterYwithE", "letterZwithM", "letterYwithM"];
	var correctLocal2 = ["E","E","M","M"];

	var globalPool2 = [letterEwithY, letterEwithZ, letterMwithY, letterMwithZ];
	var globalPoolName2 = ["letterEwithY", "letterEwithZ", "letterMwithY", "letterMwithZ"];
	var correctGlobal2 = ["E","E","M","M"];

	var startTime = Date.now();
	var endTime = startTime;
	var duration = 0;

    var stage = 0;
    var part = 0;

    var inter;
    var pressed = true;

    var that = this;

    that.hideNextButton();

    var durationArray = [];
    var nameArray = [];
    var correctArray = [];
    var pressedArray = [];
    var letterArray = [];
    //var precedingArray = [];
    var typeArray = [];

	var correctLetter = "N/A";
	var chosenLetter = "N/A";
	//var precedingLetter = "N/A";

	var i = 0;
	var n = 0;

	var pool = [localPool###pool###, globalPool###pool###];
	var correct = [correctLocal###pool###, correctGlobal###pool###];
	var letterNames = [localPoolName###pool###, globalPoolName###pool###];
	var leftLetter = leftLetter###pool###;
	var rightLetter = rightLetter###pool###;


	if(showInstr) { document.getElementById('instr').innerHTML = instr###pool###; }
	
	else
	{
		abbrev_instr1 = '<br><br><p>If an <strong>H</strong> appears, hit the <strong>number 0 key</strong>.</p><br><p>If a <strong>T</strong> appears, hit the <strong>number 1 key</strong>.</p><br><br>';
		abbrev_instr2 = '<br><br><p>If an <strong>E</strong> appears, hit the <strong>number 0 key</strong>.</p><br><p>If an <strong>M</strong> appears, hit the <strong>number 1 key</strong>.</p><br><br>';


		document.getElementById('instr').innerHTML = abbrev_instr###pool###; 

		if(pause == 0)
		{
			document.getElementById('instr').innerHTML += "<p><em>This is a timed task. It is important that you respond as <strong>quickly</strong> and <strong>accurately</strong> as possible.</em></p><br><p>When you are ready to begin, <strong>please hit the N key</strong>.</p>";
		}

		else
		{
			setTimeout(function(){
				document.getElementById('instr').innerHTML = '';
				stage = 1;
	    		if(inter === undefined) { inter = setInterval(timedFunc, 500); }
			}, pause);
		}
	}


	function endTask()
	{
    	pressed = true;
    	document.getElementById('letter').innerHTML = '';
		for(var v = 0; v < nameArray.length; v++)
		{
			name = nameArray[v];
			Qualtrics.SurveyEngine.setEmbeddedData(name+'Correct', correctArray[v]);
			Qualtrics.SurveyEngine.setEmbeddedData(name+'Response', durationArray[v]);
			Qualtrics.SurveyEngine.setEmbeddedData(name+'Pressed', pressedArray[v]);
			Qualtrics.SurveyEngine.setEmbeddedData(name+'Type', typeArray[v]);
			Qualtrics.SurveyEngine.setEmbeddedData(name+'Letter', letterArray[v]);
		}
	}
	
    function timedFunc()
    {
	    		
    	if(part % 11 == 0)
    	{ 
    		if(limitL + limitG == 0)
    		{
                stage = 0;
    			clearInterval(inter);
    			endTask();
                that.clickNextButton();
    		}

    		else
    		{
    			document.getElementById('letter').innerHTML = '<br><br>+<br><br>';
	    		if(pressed == false)
	    		{
	    			durationArray.push("N/A");
				    nameArray.push('Block' + blockNum + 'Letter' + (letterNum + 1));
				    pressedArray.push("N/A");
				    correctArray.push(correctLetter);
				    letterArray.push(chosenLetter);
				    //precedingArray.push(precedingLetter);

				    if(i = 0) { typeArray.push("local"); }
				    else if(i = 1) { typeArray.push("global"); }
				    else { typeArray.push("ERROR"); }
	    		}
    		}
    	}

    	else if(part % 11 == 1)
    	{
    		letterNum = Math.floor(part/11);

    		if(orderI == null || orderN == null)
    		{
    			i = Math.floor(Math.random() * 2);
	    		n = Math.floor(Math.random() * 4);
	    	}

	    	else
	    	{
	    		i = orderI[letterNum];
	    		n = orderN[letterNum];
	    	}

	    	//precedingLetter = chosenLetter;
	    	chosenImage = pool[i][n];
	   		chosenLetter = letterNames[i][n];
	   		correctLetter = correct[i][n];

    		if(limitL > 0 && (i == 0 || limitG == 0)) {
                limitL--;
                document.getElementById('letter').innerHTML = chosenImage;
                startTime = Date.now();
                pressed = false;
            }

    		else if(limitG > 0 && (i == 1 || limitL == 0)) {
                limitG--;
                document.getElementById('letter').innerHTML = chosenImage;
                startTime = Date.now();
                pressed = false;
            }

    		else
    		{
                stage = 0;
				clearInterval(inter);
    			endTask();
                that.clickNextButton();
    		}
    	}

    	else if(part % 11 == 4) { document.getElementById('letter').innerHTML = ''; }

    	part++;
    }
    
    
    $(document).on('keydown', function(e) {

		endTime = Date.now();

    	if(stage == 0 && e.keyCode === nextKey && (showInstr || pause == 0))
    	{
    		document.getElementById('instr').innerHTML = '';
    		stage = 1;
    		if(inter === undefined) { inter = setInterval(timedFunc, 500); }
    		pressed = true;
    	}

    	else if(stage == 1 && part % 11 != 0 && !pressed && (e.keyCode === leftKey || e.keyCode === rightKey))
    	{
    		pressed = true;
    		duration = endTime - startTime;
    		//responseTime += duration + ',';
    		//if(e.keyCode === leftKey) { key += 'left' + ','; }
    		//else if(e.keyCode === rightKey) { key += 'right' + ','; }

    		name = 'Block' + blockNum + 'Letter' + (letterNum + 1); 

		    durationArray.push(duration);
		    nameArray.push(name);
		    correctArray.push(correctLetter);
		    
    		if(e.keyCode === leftKey) { pressedArray.push(leftLetter); }
    		else if(e.keyCode === rightKey) { pressedArray.push(rightLetter); }
    		else { pressedArray.push("ERROR"); }

		    letterArray.push(chosenLetter);
		    //precedingArray.push(precedingLetter);

		    if(i = 0) { typeArray.push("local"); }
		    else if(i = 1) { typeArray.push("global"); }
		    else { typeArray.push("ERROR"); }

		    document.getElementById('letter').innerHTML = '';

    		part = part + (10-part%11);
    	}

    });
});

Qualtrics.SurveyEngine.addOnUnload(function()
{
	/*Place your JavaScript here to run when the page is unloaded*/
});