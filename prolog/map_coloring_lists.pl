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
 
neighbors(Region, OtherRegion) :- adj(Region, OtherRegion).
neighbors(Region, OtherRegion) :- adj(OtherRegion, Region).
 
init_color_groups(0, []).
init_color_groups(N, [[]|T]) :-
    N1 is N - 1,
    init_color_groups(N1, T).
 
% Constraints
 
constraint(_, []).
constraint(Region, [CurrentRegion|RestCurrentAssignment]) :-
    \+ neighbors(Region, CurrentRegion),
    constraint(Region, RestCurrentAssignment).
 
 
% Assignment
 
assign(Region, [Group|RestGroups], [[Region|Group]|RestGroups]) :-
    constraint(Region, Group).
 
assign(Region, [Group|RestGroups], [Group|NewRestGroups]) :-
    assign(Region, RestGroups, NewRestGroups).
 
assign_all_regions([], CurrentColorGroups, CurrentColorGroups).
 
assign_all_regions([Region|RestRegions], CurrentAssignment, Solution) :-
    assign(Region, CurrentAssignment, NextAssignment),
    assign_all_regions(RestRegions, NextAssignment, Solution).
 
% Entry Point
csp(Solution) :-
    regions(Regions),
    colors(Color),
    length(Color, NumColors),
    init_color_groups(NumColors, EmptyColorGroups),
    assign_all_regions(Regions, EmptyColorGroups, Solution).