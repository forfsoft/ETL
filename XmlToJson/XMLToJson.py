import xml.etree.ElementTree as ET

def XmlToJson(filepath):
    jsonData = []
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(filepath, parser)
    commentToAttribute(tree.getroot(), jsonData, None)
    return jsonData

def commentToAttribute(xmlNode, parentNode, commentText):
    if "function Comment" in str(xmlNode.tag):
        return xmlNode.text
    else:
        node = {}
        for attribute in xmlNode.attrib:
            node[attribute] = xmlNode.attrib[attribute]
        if None != commentText:
            node["comment"] = commentText
        parentNode.append(node)

        if len(xmlNode):
            childNode = []
            node[xmlNode.tag] = childNode
            for xmlChild in xmlNode:
                commentText = commentToAttribute(xmlChild, childNode, commentText)
    return None

if __name__ == '__main__':
    json = XmlToJson("test.xml")
    print(json)