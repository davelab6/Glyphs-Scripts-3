font = Glyphs.font
import re

# Set up a cubic NLI layer
# Will need to convert this to work with multiple paths
			
currentGlyph = font.selectedLayers[0].parent.name
		
def addNode(layerId, idNLI, setting):
	i = 0
	for node in font.glyphs[currentGlyph].layers[layerId].paths[0].nodes:	
		newNode = GSNode()
		newNode.x = node.x
		newNode.y = node.y
		
		if setting == 2:
			newNode.type = "offcurve"
		elif setting == 1:
			newNode.type = "line"
			font.glyphs[currentGlyph].layers[idNLI].paths.append(GSPath())
		else:
			newNode.type = "curve"
			
		font.glyphs[currentGlyph].layers[idNLI].paths[i].nodes.append(newNode)
		i = i + 1
		

def getFullName(layerName):
	for layer in font.glyphs[currentGlyph].layers:
		if re.match(layerName + ".*}$", layer.name):
			return layer.name
	

def populateNLILayer(aName, cName, dName, bName, NLIName):	
	cName = getFullName(cName)
	dName = getFullName(dName)
	bName = getFullName(bName)
	
	if font.glyphs[currentGlyph].layers[NLIName] == None:
		newNLILayer = font.glyphs[currentGlyph].layers[aName].copy()
		newNLILayer.name = NLIName
		newNLILayer.paths = []
		font.glyphs[currentGlyph].layers.append(newNLILayer)
		
	addNode(aName, NLIName, 1)
 	addNode(cName, NLIName, 2)
 	addNode(dName, NLIName, 2)
 	addNode(bName, NLIName, 3)


populateNLILayer("Regular", "C1", "D1", "B", "B NLI")
populateNLILayer("Regular Oblique", "E1", "F1", "G", "G NLI")
populateNLILayer("Bold", "H1", "I1", "J", "J NLI")
populateNLILayer("Bold Oblique", "K1", "L1", "M", "M NLI")