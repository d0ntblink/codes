// default values
PrimaryPumpSpeed := 160 - (2 * level); 
SecondaryPumpSpeed := PrimaryPumpSpeed;


// whats running 

IF pump1 AND (NOT pump2) THEN
    Pumpmode := 1;
ELSIF (NOT pump1) AND pump2 THEN
    Pumpmode := 2;
ELSIF (NOT pump1) AND (NOT pump2) THEN
    Pumpmode := 3;
ELSIF pump1 AND pump2 THEN
    Pumpmode := 4;
END_IF

// level and pump speed

IF ( automode = TRUE ) THEN
    IF level < 30.0 THEN
        PrimaryPumpSpeed := 100.00;
        SecondaryPumpSpeed := PrimaryPumpSpeed;
    END_IF
    IF ( level >= 30.0 ) AND ( level <= 50.0 ) THEN
        IF tankDrain THEN 
			SecondaryPumpSpeed := 160 - (2 * level);
            PrimaryPumpSpeed := 160 - (2 * level);
        ELSE
			PrimaryPumpSpeed := 100;
            SecondaryPumpSpeed := 100;
        END_IF
    END_IF
    IF ( level > 50.0 ) AND ( level < 70.0 ) THEN
        IF NOT tankDrain THEN
            PrimaryPumpSpeed := 100;
            SecondaryPumpSpeed := 100;
        ELSIF tankDrain THEN
            PrimaryPumpSpeed := 160 - (2 * level);
            SecondaryPumpSpeed := 0.0;
        ELSE
            PrimaryPumpSpeed := 160 - (2 * level);
            SecondaryPumpSpeed := PrimaryPumpSpeed;
        END_IF
    END_IF
    IF ( level >= 70.0 ) AND ( level <= 80.0 ) THEN
        IF ( tankDrain = FALSE ) THEN
            PrimaryPumpSpeed := 100;
            SecondaryPumpSpeed := 100;
        ELSIF tankDrain THEN
            PrimaryPumpSpeed := 20.0;
            SecondaryPumpSpeed := 0.0;
        ELSE
            PrimaryPumpSpeed := 20.0;
            SecondaryPumpSpeed := PrimaryPumpSpeed;
        END_IF
    END_IF  
    // FLAGING   
    IF level <= 30.0 THEN
	    tankDrain := FALSE;
	    halffull := FALSE;
    END_IF
    IF ( level <= 50.0 ) THEN
        IF tankDrain THEN
            halffull := TRUE;
        ELSE
            tankDrain := FALSE;
        END_IF;
    END_IF
    IF ( level >= 80.0 ) THEN
        Cycle := TRUE;
        PrimaryPumpSpeed := 0;
        SecondaryPumpSpeed := PrimaryPumpSpeed;
        tankDrain := TRUE;
        halffull := TRUE;
    END_IF
ELSIF ( automode = FALSE ) THEN
    PrimaryPumpSpeed := 0.0;
    SecondaryPumpSpeed := PrimaryPumpSpeed;
END_IF
IF  Pumpmode <> 3 THEN
    IF Pumpmode = 1 THEN
        pump1speed := PrimaryPumpSpeed;
        pump2speed := 0.0;
    ELSIF Pumpmode = 2 THEN
        pump1speed := 0;
        pump2speed := PrimaryPumpSpeed;
    ELSIF Pumpmode = 4 THEN
        // Cycle changes
        pump1speed := PrimaryPumpSpeed;
        pump2speed := SecondaryPumpSpeed;
        IF Cycle THEN
            IF ( pump1speed = 0.0 ) AND ( pump1speed = 0.0 ) THEN
                IF PrimaryPumpSpeed = pump1speed THEN
                    pump2speed := PrimaryPumpSpeed;
                    pump1speed := SecondaryPumpSpeed;
                ELSIF SecondaryPumpSpeed = pump2speed THEN
                    pump1speed := PrimaryPumpSpeed;
                    pump2speed := SecondaryPumpSpeed;
                END_IF
            END_IF
        END_IF
    END_IF;  
END_IF;

IF NOT pump1 THEN
    pump1speed := 0.0; 
END_IF;

IF NOT pump2 THEN
    pump2speed := 0.0;
END_IF;




//TRIP

//OVERLOAD
//pump1 overload detection
IF pump1speed > 0.0 THEN
    OL1timer.IN := TRUE;
ELSIF pump1speed = 0 THEN
    OL1timer.IN := FALSE;
END_IF;
//pump2 overload detection
IF pump2speed > 0.0 THEN
    OL2timer.IN := TRUE;
ELSIF pump2speed = 0 THEN
    OL2timer.IN := FALSE;
END_IF;
//OVERLOAD SOLUTION
OL1timer(PT := OL1time);
OL2timer(PT := OL2time);
IF ( OL1timer.Q ) AND  ( i1sensor ) THEN
    OL1alarm := TRUE;
END_IF;

IF ( OL2timer.Q ) AND  ( i2sensor ) THEN
    OL2alarm := TRUE;
END_IF;

//FULLTANK
IF pump1 OR pump2 THEN
	IF ( level > 95 ) THEN
        i3sensor := TRUE;
	ELSIF ( level < 95 ) THEN
        i3sensor := FALSE;
	END_IF 
END_IF;

Fulltimer(IN:= i3sensor,PT:= Fulltime);

IF pump1 OR pump2 THEN
	IF (level > 95 AND Fulltimer.Q = TRUE) THEN
        Fullalarm := TRUE;
	END_IF 
END_IF

//EMPTY RESERVOIR
IF Reslevel < 10 THEN
    EmptyRes := TRUE;
ELSE
    EmptyRes := FALSE;
END_IF
Emptytimer(IN:= EmptyRes,PT:= Emptytime);    
//TRIP ACTIVATION
IF (Emptytimer.Q) OR (Fullalarm) OR (OL1alarm) OR (OL2alarm)  THEN
    Trip := TRUE;
END_IF

//SHUTTING BOYS
IF Trip AND (( NOT OL1alarm ) OR ( NOT OL2alarm)) THEN
    pump1 := FALSE;
	pump2 := FALSE;
END_IF

IF Trip AND OL1alarm THEN
    pump1 := FALSE;
END_IF

IF Trip AND OL2alarm THEN
    pump2 := FALSE;
END_IF

//AKNOWLEDGE
IF resetButton THEN
    Trip := FALSE;
    OL1alarm := FALSE;
    OL2alarm := FALSE;
    i1sensor := FALSE;
    i2sensor := FALSE;
    i3sensor := FALSE;
    Fullalarm := FALSE;
    EmptyRes := FALSE;
    Emptytimer.IN := FALSE;
    Fulltimer.IN := FALSE;
    OL1timer.IN := FALSE;
    OL2timer.IN := FALSE;
END_IF