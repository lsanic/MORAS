
(* a *)
Goal forall x y, 
    ~(x /\ y) \/ (~x /\ y) \/ (~x /\ ~y) <-> ~(x /\ y).
Proof.
    - intros x y. split; simpl.
 -- intros [a1 | a2] b.
 --- apply a1. exact b.
 --- destruct a2 as [c | d].
 ---- now apply c.
 ---- now apply d.
 -- intros t. left. exact t.   
Qed.

(* b *)
Goal forall x y z, 
    ~(~x /\ y /\ ~z) /\ ~(x /\ y /\ z) /\ (x /\ ~y /\ ~z) 
    <-> x /\ ~y /\ ~z.
Proof.
intros; split; simpl.
-- intros a. destruct a as [a1 a2]. destruct a2 as [b1 b2]. exact b2.
-- intros e. destruct e as [e1 e2]. destruct e2 as [t1 t2]. split.
--- intros f. apply t1. apply f.   
--- split.
** intros g. apply t2. apply g.
** split.
*** exact e1.
*** now split.
Qed.