class NodeElement(object):

    def __init__(self, node):
        self.tool_id = node.attrib['ToolID']
        self.plugin = node.find('GuiSettings').attrib.get('Plugin')
        self.x_pos = float(node.find('GuiSettings').find('Position').attrib['x'])
        self.y_pos = float(node.find('GuiSettings').find('Position').attrib['y'])
        self.tool = self.plugin.split('.')[-1] if self.plugin else None

        if self.plugin == 'AlteryxBasePluginsGui.Join.Join':
            join_data = node \
                .find('Properties') \
                .find('Configuration') \
                .findall('JoinInfo')
            ljoin_data = join_data[0]
            rjoin_data = join_data[1]
            self.ljoin_fields = []
            for field in ljoin_data.findall('Field'):
                self.ljoin_fields.append(field.attrib['field'])
            self.rjoin_fields = []
            for field in rjoin_data.findall('Field'):
                self.rjoin_fields.append(field.attrib['field'])
        else:
            self.ljoin_fields = None
            self.rjoin_fields = None

        if self.plugin == 'AlteryxGuiToolkit.ToolContainer.ToolContainer':
            self.description = node \
                .find('Properties') \
                .find('Configuration') \
                .find('Caption').text
        else:
            try:
                self.description = node \
                    .find('Properties') \
                    .find('Annotation') \
                    .find('DefaultAnnotationText').text
            except:
                self.description = None

        if self.plugin == 'AlteryxBasePluginsGui.AlteryxSelect.AlteryxSelect':
            self.select_fields = node \
                .find('Properties') \
                .find('Configuration') \
                .find('SelectFields') \
                .findall('SelectField')
            self.select_fields = [field.attrib for field in self.select_fields]
        else:
            self.select_fields = None

        self.description = self.description.replace('\n', ' ') if self.description else None

        self.data = {
            'Tool ID': self.tool_id,
            'Plugin': self.plugin,
            'Tool': self.tool,
            'Description': self.description,
            'x': self.x_pos,
            'y': self.y_pos,
            'Left Join Fields': self.ljoin_fields,
            'Right Join Fields': self.rjoin_fields,
            'Select Fields': self.select_fields
        }
