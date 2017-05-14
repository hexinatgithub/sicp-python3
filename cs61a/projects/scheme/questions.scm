(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.
(define (map proc items)
    (if (null? items) nil
        (cons (proc (car items)) (map proc (cdr items)))
))

(define (cons-all first rests)
    (map (lambda (x) (cons first x) rest)))

(define (zip pairs)
    (list ((map car pairs) (map cadr pairs)))
)

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s) (helper 0 s))


(define (helper k s)
    (if (null? s)
        s
        (cons (cons k (cons (car s) nil)) (helper (+ k 1) (cdr s)))
    )
)

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
(define (helper amount coins history)
  (cond
    ((= amount 0) (list history))
    ((null? coins) nil)
    ((< amount 0) nil)
    (else (append
      (helper (- amount (car coins)) coins (append history (cons (car coins) nil)))
      (helper amount (cdr coins) history)
      ))
  ))
  (helper total denoms nil)
)

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons form (cons params (let-to-lambda body)))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons (cons 'lambda (cons (let-to-lambda (map car values)) (let-to-lambda body))) (let-to-lambda (map cadr values)))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))