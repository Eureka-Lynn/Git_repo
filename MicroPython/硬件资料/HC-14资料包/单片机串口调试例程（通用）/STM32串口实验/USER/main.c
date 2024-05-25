#include "led.h"
#include "delay.h"
#include "key.h"
#include "sys.h"
#include "usart.h"
 

//**** 声明 ********************************************************************
/*******************************************************************************
 * 下面来自互联开源程序，由广州汇承信息科技有限公司收集
 * 方便用户参考学习，本公司不对单片机做编程指导，请用户自行研究
 * 程序仅供测试参考，不能应用在实际工程中，不一定能通过编译
 * 公司网站  http://www.hc01.com/
 * 淘宝网址  http://hc-com.taobao.com/
*******************************************************************************/


 int main(void)
 {	
	delay_init();	    	 //延时函数初始化	  
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2); //设置NVIC中断分组2:2位抢占优先级，2位响应优先级
	uart_init(9600);	 //串口初始化为9600
 	LED_Init();			     //LED端口初始化
 	while(1)
	{
		LED0=1;
		LED1=0;
		//delay_us(500);
		delay_ms(2);
		LED0=0;
		LED1=1;
		//delay_us(500);
		delay_ms(2);
	}
 }

