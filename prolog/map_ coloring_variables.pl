% csp model
regions([wa, nt, sa, q, nsw, v]).
colors([red, green, blue]).
 
adj(wa, nt).
adj(sa, wa).
adj(nt, sa).
adj(nt, q).
adj(sa, q).
adj(q, nsw).
adj(sa, nsw).
adj(nsw, v).
adj(sa, v).
 
% Helpers
 
neighbors(Region, OtherRegion) :-
   adj(OtherRegion, Region).
 
neighbors(Region,OtherRegion) :-
   adj(Region, OtherRegion).
 
% Constraints
 
constraint(_, []).
 
constraint(Region/Color, [OtherRegion/_|RestAssignment]):-
   \+ neighbors(Region, OtherRegion),
   constraint(Region/Color, RestAssignment).
 
constraint(Region/Color, [OtherRegion/OtherColor|RestAssignment]) :-
   neighbors(Region, OtherRegion),
   Color \= OtherColor,
   constraint(Region/Color, RestAssignment).
 
% Assignment
 
assign([], Solution, Solution).
 
assign([Region|OtherRegions], CurrentAssignment, Solution) :-
   colors(Colors),
   member(Color, Colors),
   constraint(Region/Color, CurrentAssignment),
   assign(OtherRegions, [Region/Color|CurrentAssignment], Solution).
 
% Entry Point
csp(Solution) :-
   regions(Regions),
   assign(Regions, [], Solution).