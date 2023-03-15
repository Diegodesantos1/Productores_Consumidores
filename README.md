<h1 align = "center">Productores y consumidores</h1>

En este [repositorio](https://github.com/Diegodesantos1/Productores_Consumidores) queda resuelto el ejercicio del barbero durmiente.

<h2 align = "center">Planteamiento del problema</h2>

*La competencia por un recurso en memoria es un estado mediante en el cual uno o varios procesos tienen dependencia de algún recurso que podría no estar disponible en algún momento.*

*La dependencia de recursos en el estado con un solo proceso generalmente es secuencial, en donde el proceso dependiente tiene que consumir ciclos de reloj en espera de la liberación del recurso que necesita para continuar con su procesamiento.* 

*No obstante el tiempo de ejecución en el panorama secuencial se puede alargar mucho más cuando el recurso tarda en llegar o bien por labores de intentos de sincronización fuera de tiempo. Por tal motivo uno de los primeros planteamientos realizados para evitar la competencia de recursos es el uso de hilos de ejecución (threads) con la capacidad de comunicarse entre sí a través de un procedimiento de exclusión mutua. Sin embargo el mecanismo es pensado en un solo procesador.* 

*Más adelante nacieron los procesadores multicore, en donde cada core es capaz de ejecutar instrucciones independientes uno de otro, lo cuál ha modificado el esquema tradicional de programación secuencial. Aquí es donde nace el concepto de programación paralela.* 

*Un programa paralelo tiene la capacidad de ejecutar instrucciones en el mismo ciclo de reloj, pero para preservar sus beneficios de reducir enormemente los tiempos de ejecución, éstas instrucciones deben ser independientes de ejecución, es decir, reducir la sincronización hacia el mínimo de comunicación cuando existe dependencia de recursos, distribución de recursos en los procesadores y los mecanismos de exclusión mutua. Existen varios procedimientos de exclusión mutua.* 

*Un ejemplo clásico es el uso de semáforos en productores y consumidores y también han surgido otros problemas en base al acceso concurrente.*

*El acceso concurrente por parte de procesos productores y consumidores sobre un recurso común se realiza por medio un buffer de elementos. Los productores tratan de introducir elementos en el buffer de uno en uno, y los consumidores tratan de extraer elementos de uno en uno.*

*Para ejemplificar el desarrollo de un programa para productores y consumidores, asumimos que el productor es el que genera los recursos que van a utilizar los consumidores, por lo tanto los consumidores necesitan un proceso de sincronización con el productor para saber cuando el momento de consumir ha llegado.*

<h2 align = "center">Código</h2>
