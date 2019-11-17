import AfterburnNode as abnode
import time
from random import randrange

def main():
    nodes = createNodes()
    count = 10
    resparkNode = None
    eventTime = 12
    nearSparkFactor = 0.6
    intermediateSparkFactor = 0.2
    farSparkFactor = 0.1

    while True:
        for node in nodes:
            response = node.sendNextPackage()
            if response is None:
                return
            if response is not 200:
                print response
        if count % eventTime == 0:
            count = 0
            if resparkNode is None:
                nodeCount = len(nodes)
                resparkNode = randrange(0, nodeCount-1)
                nodes[resparkNode].resparking = True
                nodes[resparkNode].sparkFactor = 1
                nodes[(resparkNode+1) % nodeCount].sparkFactor = nearSparkFactor
                nodes[(resparkNode+1) % nodeCount].resparking = True
                nodes[(resparkNode-1) % nodeCount].sparkFactor = nearSparkFactor
                nodes[(resparkNode-1) % nodeCount].resparking = True
                nodes[(resparkNode-2) % nodeCount].sparkFactor = intermediateSparkFactor
                nodes[(resparkNode-2) % nodeCount].resparking = True
                nodes[(resparkNode+2) % nodeCount].sparkFactor = intermediateSparkFactor
                nodes[(resparkNode+2) % nodeCount].resparking = True
                nodes[(resparkNode-3) % nodeCount].sparkFactor = farSparkFactor
                nodes[(resparkNode-3) % nodeCount].resparking = True
                nodes[(resparkNode+3) % nodeCount].sparkFactor = farSparkFactor
                nodes[(resparkNode+3) % nodeCount].resparking = True
            else:
                nodeCount = len(nodes)
                nodes[resparkNode].resparking = False
                nodes[(resparkNode-1) % nodeCount].resparking = False
                nodes[(resparkNode+1) % nodeCount].resparking = False
                nodes[(resparkNode-2) % nodeCount].resparking = False
                nodes[(resparkNode+2) % nodeCount].resparking = False
                nodes[(resparkNode-3) % nodeCount].resparking = False
                nodes[(resparkNode+3) % nodeCount].resparking = False
                resparkNode = None

        count += 1
        time.sleep(3)

def createNodes():
    nodes = []
    nodes.append(abnode.AfterburnNode(1, 'Rf9EgMf)rkI8w2)i+Z'))
    nodes.append(abnode.AfterburnNode(2, '60-d0!D+B4cwd2P0&J'))
    nodes.append(abnode.AfterburnNode(3, '7hLqT6qE!fpX@1Zc!Q'))
    nodes.append(abnode.AfterburnNode(4, 'B77zKLfqIciCQ0AXgv'))
    nodes.append(abnode.AfterburnNode(5, 'g_F@J-5JgKj4&J4qwZ'))
    nodes.append(abnode.AfterburnNode(6, '2W&KSY4tIa(918Pi2C'))
    nodes.append(abnode.AfterburnNode(7, '7MQ+C2A*F(aZ)_OAUm'))
    nodes.append(abnode.AfterburnNode(8, '_ps4JfU)RO2Xisilfu'))
    nodes.append(abnode.AfterburnNode(9, '6vJ)tWE7HfI)65x2(!'))
    nodes.append(abnode.AfterburnNode(10, '-drKi9hCniPB&n25Li'))
    nodes.append(abnode.AfterburnNode(11, '4+cwXaLb(x7HMv2IrO'))
    nodes.append(abnode.AfterburnNode(12, 'UIhUdnzi0*z9-hy&Gu'))
    nodes.append(abnode.AfterburnNode(13, '5WuGv-slukCPX+V@HK'))
    nodes.append(abnode.AfterburnNode(14, 'POUW_gHk+-jd4q_*)C'))
    nodes.append(abnode.AfterburnNode(15, 'ry!C3Dh9ame5hLAx15'))

    return nodes

if __name__ == "__main__":
    main()
