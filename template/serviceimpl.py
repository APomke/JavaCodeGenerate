serviceimpl_template_str = """
package {{ package_name }}.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import {{ package_name }}.mapper.{{ mapper_name }};
import {{ package_name }}.entity.{{ entity_name }};
import {{ package_name }}.service.{{ service_name }};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


@Service
public class {{ class_name }} extends ServiceImpl<{{ mapper_name }}, {{ entity_name }}> implements {{ service_name }} {
    
    @Autowired
    private {{ mapper_name }} {{ entity_name | lower }}Mapper;
    // 查询
    public {{ entity_name }} get{{ entity_name }}(int id) {
        return {{ entity_name | lower }}Mapper.selectById(id);
    }
    {% for entity in entity_list %}
    
    @Override
    {% if entity.name == 'id' %}
    public {{ entity_name }} get{{ entity_name }}By{{ entity.name_first }}({{ entity.type }} {{ entity.name }}) {
        QueryWrapper<{{ entity_name }}> queryWrapper = new QueryWrapper<>();
        return {{ entity_name | lower }}Mapper.selectById(queryWrapper);
    }
    {% else %}
    public List<{{ entity_name }}> get{{ entity_name }}ListBy{{ entity.name_first }}({{ entity.type }} {{ entity.name }}) {
        QueryWrapper<{{ entity_name }}> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("{{ entity.name_first | lower }}",{{ entity.name }});
        return {{ entity_name | lower }}Mapper.selectList(queryWrapper);
    }
    {% endif %}
    {%- endfor %}
    
    // 修改
    @Override
    public int update{{ entity_name }}({{ entity_name }} {{ entity_name | lower }}) {
        return {{ entity_name | lower }}Mapper.updateById({{ entity_name | lower }});
    }
    
    // 增加
    @Override
    public int add{{ entity_name }}({{ entity_name }} {{ entity_name | lower }}) {
        return {{ entity_name | lower }}Mapper.insert({{ entity_name | lower }});
    }
    
    // 删除
    @Override
    public int delete{{ entity_name }}(String id) {
        return {{ entity_name | lower }}Mapper.deleteById(id);
    }
}
"""