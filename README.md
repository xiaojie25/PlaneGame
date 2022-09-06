+ 定时器 

pygame中的定时器的使用

在pygame中可以使用`pygame.time.set_timer`来添加定时器所谓定时器就是每隔一段时间，去执行一些动作 `set_timer(eventid,millsecond)`

`set_timer`可以创建一个事件

在游戏循环的事件监听方法中捕获到该事件

第一个参数事件代号需要基于常量`pygame.USEREVENT`来指定

`USEREVENT`是一个整数，在发生事件的事件可以用`USEREVENT+1`来指定，以此类推

+ KILL

`kill`方法可以删除精灵对象以及精灵对象所在的精灵组的内容。

***及时的删除精灵对象，可以及时的释放内存***