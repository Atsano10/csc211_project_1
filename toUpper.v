`timescale 1ns / 1ps

module toUpper(a,b);
    input [7:0] a;
    output [7:0] b;

    wire na7, na6, na4, na3, na2, na1, na0;
    wire t1, t2, t3, t4, t5;
    
    not #5 (na7, a[7]); 
    not #5 (na6, a[6]);
    not #5 (na4, a[4]);
    not #5 (na3, a[3]);
    not #5 (na2, a[2]);
    not #5 (na1, a[1]);
    not #5 (na0, a[0]);

    and #10 (t1, a[7], a[6]);
    and #10 (t2, na7, na6, a[5]);
    and #10 (t3, na7, a[6], a[5], a[4], a[3],a[2]);
    and #10 (t4, na7, a[6], a[5],a[4],a[3],na2,a[1],a[0]);
    and #10 (t5, na7, a[5], na4, na3, na2, na1, na0);

    or #10 (b[5],t1,t2,t3,t4,t5);

    buf #4 (b[0], a[0]);
    buf #4 (b[1], a[1]);
    buf #4 (b[2], a[2]);
    buf #4 (b[3], a[3]);
    buf #4 (b[4], a[4]);
    buf #4 (b[6], a[6]);
    buf #4 (b[7], a[7]);

endmodule
