(*
	Eight Queens puzzle in Object Pascal
	Written by Tim Budd, Oregon State University, 1996
*)
Program EightQueen;

type 
	Queen = object
		(* data fields *)
		row : integer;
		column : integer;
		neighbor : Queen;
		
			(* initialization *)
		procedure initialize (col : integer; ngh : Queen);
		
			(* operations *)
		function canAttack (testRow, testColumn : integer) : boolean;
		function findSolution : boolean;
		function advance : boolean;
		procedure print;
	end;
	
var
	neighbor, lastQueen : Queen;
	i : integer;

procedure Queen.initialize (col : integer; ngh : Queen);
begin
		(* initialize our column and neighbor values *)
	column := col;
	neighbor := ngh;
		
		(* start in row 1 *)
	row := 1;	
end;

function Queen.canAttack (testRow, testColumn : integer) : boolean;
var
	can : boolean;
	columnDifference : integer;
begin
		(* first see if rows are equal *)
	can := (row = testRow);
	
	if not can then begin
		columnDifference := testColumn - column;
		if (row + columnDifference = testRow) or
			(row - columnDifference = testRow) then
				can := true;
		end;
		
	if (not can) and (neighbor <> nil) then
		can := neighbor.canAttack(testRow, testColumn);
	canAttack := can;	
end;

function queen.findSolution : boolean;
var 
	done : boolean;
begin
	done := false;
	findSolution := true;
	
		(* test positions *)
	if neighbor <> nil then
		while not done and neighbor.canAttack(row, column) do
			if not self.advance then begin
				findSolution := false;
				done := true;
				end;				
end;

function queen.advance : boolean;
begin
	advance := false;
	
		(* try next row *)
	if row < 8 then begin
		row := row + 1;
		advance := self.findSolution;
	end
	else begin
	
			(* can not go further *)
			(* move neighbor to next solution *)
		if neighbor <> nil then
			if not neighbor.advance then
				advance := false
			else begin
				(* start again in row 1 *)
				row := 1;
				advance := self.findSolution;
			end;
	end;
end;

procedure queen.print;
begin
	if neighbor <> nil then
		neighbor.print;
	writeln('row ', row , ' column ', column);	
end;
	
begin
	neighbor := nil;
	for  i := 1 to 8 do begin
			(* create and initialize new queen *)
		new (lastqueen);
		lastQueen.initialize (i, neighbor);
		if not lastQueen.findSolution then
			writeln('no solution');
			(* newest queen is next queen neighbor *)
		neighbor := lastQueen;
	end;
	
	lastQueen.print;
	
	for i := 1 to 8 do begin
		neighbor := lastQueen.neighbor;
		dispose (lastQueen);
		lastQueen := neighbor;
	end;
end.