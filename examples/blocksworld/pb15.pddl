(define (problem pb15)
   (:domain blocksworld)
   (:objects a b c d e f g h i j k l m n o)
   (:init (onTable a) (onTable b) (onTable c) (onTable d) (onTable e) 
          (onTable f) (onTable g) (onTable h) (onTable i) (onTable j)
          (onTable k)  (onTable l)  (onTable m) (onTable n)
          (onTable o)
          (clear a)  (clear b) (clear c) (clear d) (clear e) (clear j) 
          (clear f)  (clear g) (clear h) (clear i) (clear k) (clear l) 
          (clear m) (clear n) (clear o)
          (equal a a) (equal b b) (equal c c) (equal d d) (equal e e)
          (equal f f) (equal g g) (equal h h) (equal i i) (equal j j)
          (equal k k) (equal l l) (equal m m) (equal n n) (equal o o)
          (handempty)
          )
   (:goal (and (on a b) (on b c) (on c d) (on d e) (on e f) (on f g)
               (on g h) (on h i) (on i j) (on j k) (on k l)(on l m)
               (on m n) (on n o))))