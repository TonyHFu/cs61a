(define (nats start)
    (cons-stream start (nats (+ start 1)))
    
    )

(define (add-stream s1 s2)
    (cons-stream (+ (car s1) (car s2)) add-stream((cdr-stream s1) (cdr-stream s2)))
    
    )

(define ones (cons-stream 1 ones))

(define ints (cons-stream 1 (add-stream ints ones)))

(define (stream-to-list s num-elements)
    (if (or (null? s) (= num-elements 0))
        nil
        (cons (car s) (stream-to-list(cdr-stream s) (- num-elements 1)))
        
        )
    
    )

(define (add k s) (cons-stream (+ k (car s)) (add k (cdr-stream s))))

(define not-three  (cons-stream 1 (cons-stream 2 (add 3 not-three))))



