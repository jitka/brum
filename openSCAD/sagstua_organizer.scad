tloustka_dreva = 5;
u_matrace = 20;
sirka_bocnice = 21;
hloubka_knizky = 45;
hloubka_nabijecky = 135; // 145 se nevejde do sliceru
vyska_nabijecky = 50;
vyska_bocnice = 140;
pod_bocnici = 30;
vyska = 190;

module lko(){
    hloubka_po_knizku = tloustka_dreva + hloubka_knizky + tloustka_dreva + sirka_bocnice + u_matrace;
    hloubka_dilu = tloustka_dreva + hloubka_nabijecky + hloubka_po_knizku;
    difference() {
        square([hloubka_dilu, vyska]);
        translate([hloubka_po_knizku,pod_bocnici+vyska_nabijecky,0])
        square([hloubka_dilu - hloubka_po_knizku, vyska-pod_bocnici-vyska_nabijecky]);
    }
}

module bocnice(){
   rost = 4;
   sirka_rostu = 100;
   dole = 20 - rost/2;
   translate([sirka_bocnice/2, sirka_bocnice/2, 0])circle(sirka_bocnice/2);
   translate([sirka_bocnice/2, vyska_bocnice-sirka_bocnice/2, 0])circle(sirka_bocnice/2);
   translate([0,sirka_bocnice/2,0])square([sirka_bocnice, vyska_bocnice-sirka_bocnice]);
   translate([-sirka_rostu/2,dole,0])square([sirka_rostu,rost],center=true);
}

module bocni_dil_2d(){
   difference() {
      lko();
      translate([u_matrace, pod_bocnici,0])bocnice();
   }
}

module bocni_dil(){
    linear_extrude(height=tloustka_dreva){
        bocni_dil_2d();
    }
}

bocni_dil();

