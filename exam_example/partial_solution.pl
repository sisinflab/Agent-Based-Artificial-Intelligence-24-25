% csp model

pet([jack, melody, zara, diego, leo, cacco, lil, camillo]).
area([area1, area2, area3]).

dog([jack, melody, zara, diego, leo]).
rabbit([cacco, lil, camillo]).
male([jack, diego, leo, camillo]).
female([melody, zara, cacco, lil]).


% first constraint

check_female(_, []).

check_female(Area, [Pet/Area|RestCurrentAssignment]) :-
    female(Female),
    member(Pet, Female),
    check_female(Area, RestCurrentAssignment).

check_female(Area, [Pet/Area|RestCurrentAssignment]) :-
    Pet = diego,
    check_female(Area, RestCurrentAssignment).

check_female(Area, [_/OtherArea|RestCurrentAssignment]) :-
    Area \= OtherArea,
    check_female(Area, RestCurrentAssignment).

diego_constraint([], _).

diego_constraint([diego/Area|_], CurrentAssignment) :-
    check_female(Area, CurrentAssignment).

diego_constraint([Pet/_|RestCurrentAssignment], CurrentAssignment) :-
    Pet \= diego,
    diego_constraint(RestCurrentAssignment, CurrentAssignment).

constraints(CurrentAssignment) :-
    diego_constraint(CurrentAssignment, CurrentAssignment).

% assignment logic

assign([], Solution, Solution).

assign([Pet|RestPets], CurrentAssignment, Solution) :-
    area(Areas),
    member(Area, Areas),
    constraints([Pet/Area|CurrentAssignment]),
    assign(RestPets, [Pet/Area|CurrentAssignment], Solution).

csp(Solution) :-
    pet(Pets),
    assign(Pets, [], Solution).