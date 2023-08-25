#lang racket
(provide (all-defined-out))
(+ 2 2)
; defining a function
(define (adder x y)
  (+ x y))
; defining a power function
(define (pow1 x y) ; x to the yth power 
  (if (= y 0)
      1
      (* x (pow1 x (- y 1)))))

(define x 2) ; just like defining x = 2
; making a calculator using if statements 
(define (calculator x y z) ; z is for defining which function you would use 
  
    (if (= z 1) ; 1 for add
        (+ x y)
        (if (= z 2); 2 for sub
            (- x y)
            (if (= z 3); 3 for multiply
                (* x y)
                (/ x y))))); 4 for divide 
